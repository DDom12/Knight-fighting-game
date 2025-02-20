import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def heal(self):
        if self.health < 120:
            self.health = min(self.health + 20, 120)
            return f"{self.name} healed: {self.health} HP"
        return f"{self.name} can't heal more!"

    def attack(self, opponent):
        if opponent.health > 0:
            opponent.health = max(opponent.health - self.damage, 0)
            return f"{opponent.name} took damage: {opponent.health} HP"
        return f"{opponent.name} has already been defeated!"

Knight1 = Player("Knight1", 100, 20)
Knight2 = Player("Knight2", 100, 20)

class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game Controls")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()


        self.knight1_label = QLabel(f"Knight1 HP: {Knight1.health}")
        self.knight2_label = QLabel(f"Knight2 HP: {Knight2.health}")
        self.layout.addWidget(self.knight1_label)
        self.layout.addWidget(self.knight2_label)

        self.button_heal_k1 = QPushButton("Heal Knight1")
        self.button_heal_k1.clicked.connect(self.heal_knight1)
        self.layout.addWidget(self.button_heal_k1)

        self.button_attack_k2 = QPushButton("Attack Knight2")
        self.button_attack_k2.clicked.connect(self.attack_knight2)
        self.layout.addWidget(self.button_attack_k2)

        self.button_heal_k2 = QPushButton("Heal Knight2")
        self.button_heal_k2.clicked.connect(self.heal_knight2)
        self.layout.addWidget(self.button_heal_k2)

        self.button_attack_k1 = QPushButton("Attack Knight1")
        self.button_attack_k1.clicked.connect(self.attack_knight1)
        self.layout.addWidget(self.button_attack_k1)

        self.setLayout(self.layout)

    def update_labels(self):

        self.knight1_label.setText(f"Knight1 HP: {Knight1.health}")
        self.knight2_label.setText(f"Knight2 HP: {Knight2.health}")

    def check_winner(self):

        if Knight1.health == 0:
            self.knight1_label.setText("Knight1 LOST!")
            self.disable_buttons()
        elif Knight2.health == 0:
            self.knight2_label.setText("Knight2 LOST!")
            self.disable_buttons()

    def disable_buttons(self):

        self.button_heal_k1.setDisabled(True)
        self.button_attack_k2.setDisabled(True)
        self.button_heal_k2.setDisabled(True)
        self.button_attack_k1.setDisabled(True)


    def heal_knight1(self):
        print(Knight1.heal())
        self.update_labels()

    def attack_knight2(self):
        print(Knight1.attack(Knight2))
        self.update_labels()
        self.check_winner()

    def heal_knight2(self):
        print(Knight2.heal())
        self.update_labels()

    def attack_knight1(self):
        print(Knight2.attack(Knight1))
        self.update_labels()
        self.check_winner()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GameGUI()
    game.show()
    sys.exit(app.exec_())
