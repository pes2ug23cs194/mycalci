"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""
import sys
import click
from calculator import add, subtract, multiply, \
                       divide, power, square_root

@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        if operation == 'add':
            if num2 is None:
                raise ValueError("Operation 'add' requires two numbers.")
            result = add(num1, num2)
        elif operation == 'subtract':
            if num2 is None:
                raise ValueError("Operation 'subtract' requires two numbers.")
            result = subtract(num1, num2)
        elif operation == 'multiply':
            if num2 is None:
                raise ValueError("Operation 'multiply' requires two numbers.")
            result = multiply(num1, num2)
        elif operation == 'divide':
            if num2 is None:
                raise ValueError("Operation 'divide' requires two numbers.")
            result = divide(num1, num2)
        elif operation == 'power':
            if num2 is None:
                raise ValueError("Operation 'power' requires two numbers.")
            result = power(num1, num2)
        elif operation == 'sqrt':
            if num2 is not None:
                click.echo("Warning: 'sqrt' operation ignores the second number.")
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result nicely
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except TypeError:
        # Catch the error if num2 is None and a two-operand function is called
        click.echo(f"Error: Operation '{operation}' requires a second number.")
        sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    calculate()