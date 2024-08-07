variable "lambda_function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = "my_lambda_function"
}

variable "lambda_handler" {
  description = "The handler for the Lambda function"
  type        = string
  default     = "main.start_lambda"
}

variable "lambda_runtime" {
  description = "The runtime for the Lambda function"
  type        = string
  default     = "python3.8"
}

variable "eventbridge_rule_name" {
  description = "The name of the EventBridge rule"
  type        = string
  default     = "my_eventbridge_rule"
}

variable "schedule_expression" {
  description = "The schedule expression for the EventBridge rule"
  type        = list(string)
  default     = [
    "cron(0/15 6-19 ? * MON-FRI *)",
    "cron(0 0,3,21,23 ? * MON-FRI *)",
    "cron(0 0,3,21,23 ? * SAT,SUN *)"
  ]
}

variable "time_window_minutes" {
  description = "The time window in minutes for the schedule (e.g., 15 for every 15 minutes)"
  type        = number
  default     = 15
}
