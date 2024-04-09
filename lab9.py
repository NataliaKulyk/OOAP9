import random

# Originator
class Conversation:
    def __init__(self):
        self._state = []  # Створюємо список для збереження слів

    def add_words(self, words):
        self._state.append(words)  # Додаємо слова до списку

    def get_current_state(self):
        return ' '.join(self._state)  # Повертаємо поточний стан розмови у вигляді рядка, розділеного пробілами

    def restore_state(self, memento):
        if memento:
            self._state = memento.get_saved_state()  # Відновлюємо стан розмови з переданого memento

    def save_state(self):
        return Memento(self._state.copy())  # Зберігаємо поточний стан розмови у вигляді memento

# Memento
class Memento:
    def __init__(self, state):
        self._state = state  # Зберігаємо стан розмови

    def get_saved_state(self):
        return self._state  # Повертаємо збережений стан розмови

# Caretaker
class Caretaker:
    def __init__(self):
        self._mementos = []  # Створюємо список для зберігання memento

    def add_memento(self, memento):
        self._mementos.append(memento)  # Додаємо memento до списку

    def get_memento(self, steps_back=1):
        if steps_back <= len(self._mementos):
            return self._mementos[-steps_back]  # Повертаємо memento, яке знаходиться на вказаній кількості кроків назад
        else:
            return None  # Повертаємо None, якщо немає достатньо memento для відновлення

    def remove_memento(self, memento):
        if memento in self._mementos:
            self._mementos.remove(memento)  # Видаляємо memento зі списку, якщо воно там є

# Simulation
def simulate_conversation(conversation, caretaker):
    words = ['hello', 'world', 'goodbye', 'python', 'programming']
    for _ in range(10):
        word = random.choice(words)  # Вибираємо випадкове слово
        conversation.add_words(word)  # Додаємо слово до розмови
        memento = conversation.save_state()  # Зберігаємо поточний стан розмови
        caretaker.add_memento(memento)  # Додаємо memento до Caretaker
        print(f"Added word: {word}")  # Виводимо додане слово

    print("\nConversation:")
    print(conversation.get_current_state())  # Виводимо поточний стан розмови

    print("\nUndo 3 words:")
    for _ in range(3):
        memento = caretaker.get_memento()  # Отримуємо memento для відміни
        conversation.restore_state(memento)  # Відновлюємо стан розмови з memento
        caretaker.remove_memento(memento)  # Видаляємо використане memento з Caretaker

    print("\nConversation after undo:")
    print(conversation.get_current_state())  # Виводимо стан розмови після відміни

conversation = Conversation()  # Створюємо об'єкт розмови
caretaker = Caretaker()  # Створюємо об'єкт Caretaker
simulate_conversation(conversation, caretaker)  # Викликаємо функцію для симуляції розмови
