provider "aws" {
  region = "us-west-2" # Update as necessary
}

# Create the IAM role for Lambda
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Attach the AWSLambdaBasicExecutionRole managed policy
resource "aws_iam_role_policy_attachment" "lambda_exec" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Create a zip file of all Python files in the src directory
data "archive_file" "lambda_package" {
  type        = "zip"
  source_dir  = "${path.module}/../src"
  output_path = "${path.module}/../src/main.zip"
}

# Create the Lambda function
resource "aws_lambda_function" "my_lambda" {
  function_name = var.lambda_function_name
  handler       = var.lambda_handler
  runtime       = var.lambda_runtime
  role          = aws_iam_role.lambda_exec_role.arn

  filename         = data.archive_file.lambda_package.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_package.output_path)

  environment {
    variables = {
      DATABASE_URL = "https://mydatabase.example.com"
      API_KEY      = "my-api-key"
      LOG_LEVEL    = "DEBUG"
    }
  }

  depends_on = [aws_iam_role_policy_attachment.lambda_exec]
}

# Create EventBridge rules and targets
resource "aws_cloudwatch_event_rule" "my_eventbridge_rule" {
  count               = length(var.schedule_expression)
  name                = "${var.eventbridge_rule_name}-${count.index}"
  schedule_expression = var.schedule_expression[count.index]
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  count = length(var.schedule_expression)

  rule      = aws_cloudwatch_event_rule.my_eventbridge_rule[count.index].name
  target_id = "lambda-${count.index}"
  arn       = aws_lambda_function.my_lambda.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  count = length(var.schedule_expression)

  statement_id  = "AllowExecutionFromEventBridge-${count.index}"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.my_eventbridge_rule[count.index].arn
}

output "lambda_function_arn" {
  value = aws_lambda_function.my_lambda.arn
}
