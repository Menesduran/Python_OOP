"""
software_developers.py

In-class exercise: Module containing the SoftwareDeveloper class.
"""

class SoftwareDeveloper:
    def __init__(self, name: str, age: int, experience_years: int) -> None:
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.knowledge_languages: list[str] = []

    def show_info(self) -> str:
        """Return the developer's information as a formatted string."""
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Experience Years: {self.experience_years}\n"
            f"Knowledge Languages: {self.knowledge_languages}"
        )

    def add_language(self, language: str) -> str:
        """Add one or more comma-separated languages to the known list."""
        for item in language.split(","):
            cleaned = item.strip()
            if cleaned:
                self.knowledge_languages.append(cleaned)

        return f"{language} added to knowledge languages list."


if __name__ == "__main__":
    dev1 = SoftwareDeveloper(name="John Doe", age=30, experience_years=5)
    dev1.add_language(language="C")
    print(dev1.show_info())
    print()

    dev2 = SoftwareDeveloper(name="Jane Smith", age=28, experience_years=3)
    dev2.add_language(language="Python, Java, C++")
    print(dev2.show_info())