import re
import sys


def process_table(table):
    lines = table.strip().split("\n")
    total_pattern = re.compile(r"\*\*Total\*\*")
    updated_lines = []
    weekly_sum = 0

    for line in lines:
        if total_pattern.search(line):
            # Skip total line for now
            continue

        # Extract the values from the table row
        parts = re.split(r"\s+\|\s+", line.strip("| "))
        row_values = []

        for value in parts[1:]:  # Skip day name
            # Check if the value contains additions like 18.07+26.98+20.44
            if "+" in value:
                value = sum(map(float, value.split("+")))
            else:
                value = float(value) if value != "0" else 0
            row_values.append(value)

        # Update the total for Week 1 (or any week where non-zero values are found)
        weekly_sum += row_values[0]
        updated_lines.append(f"| {parts[0]:<9} | {' | '.join(map(str, row_values))} |")

    # Append the updated total line
    updated_lines.append(
        f"| **Total**  | **${weekly_sum:.2f}** | **$0** | **$0** | **$0** |"
    )

    return "\n".join(updated_lines)


def main():
    # Read input (via stdin)
    input_table = sys.stdin.read()
    # Process the table and print the updated table
    updated_table = process_table(input_table)
    print(updated_table)


if __name__ == "__main__":
    main()
