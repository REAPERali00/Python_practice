class Card:
    def __init__(self, msg: str, card_length: int = 30, height_ratio: float = 0.5):
        self.msg = msg
        self.card_length = card_length
        self.card_height = max(3, int(card_length * height_ratio))

    def convert_str_line(self, line: str) -> str:
        total_padding = self.card_length - 2 - len(line)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        return f"|{' '* left_padding}{line}{' '* right_padding}|"

    def convert_lines(self) -> list:
        words = self.msg.split()
        current_line = ""
        lines = []

        for word in words:
            if len(current_line) + len(word) + 1 <= self.card_length - 4:
                current_line += (" " if current_line else "") + word
            else:
                lines.append(self.convert_str_line(current_line))
                current_line = word
        lines.append(self.convert_str_line(current_line))
        return lines

    def print_card(self):
        top_line = "+" + "-" * (self.card_length - 2) + "+\n"
        empty_line = "|" + " " * (self.card_length - 2) + "|\n"
        content_lines = self.convert_lines()

        tot_empty_lines = self.card_height - len(content_lines)
        top_pad = tot_empty_lines // 2
        bot_pad = tot_empty_lines - top_pad

        card = (
            top_line
            + empty_line * top_pad
            + "\n".join(content_lines)
            + "\n"
            + empty_line * bot_pad
            + top_line
        )
        print(card)
