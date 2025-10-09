"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click

# Assuming these functions exist and are importable
from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        # Check for missing second operand for two-number operations
        if operation in ["add", "subtract", "multiply", "divide", "power"]:
            if num2 is None:
                raise ValueError(f"Operation '{operation}' requires two numbers.")

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "sqrt":
            if num2 is not None:
                # Optionally warn, but proceed with single operand
                # click.echo("Warning: 'sqrt' operation ignores the second number.", err=True)
                pass
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result nicely
        if result == int(result):
            click.echo(int(result))
        else:
            # Use a slightly less precise format for general float output
            click.echo(f"{result}")

    except ValueError as e:
        # Catches validation errors like missing operands (now explicitly raised above)
        # or division by zero/sqrt of negative (from the calculator module)
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Fallback for truly unexpected errors
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
