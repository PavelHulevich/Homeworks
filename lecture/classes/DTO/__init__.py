from dataclasses import dataclass, field

@dataclass
class StudentDto:
    first_name: str
    last_name: str
    age: int
    course: int
    average_score: float

    def __post_init__(self):
        if not self.first_name.isalpha() or not self.first_name.istitle():
            raise ValueError("First name must contain only letters and start with a capital letter")
        if not self.last_name.isalpha() or not self.last_name.istitle():
            raise ValueError("Last name must contain only letters and start with a capital letter")
        if not 18 <= self.age <= 30:
            raise ValueError("Age must be between 18 and 30")
        if not 1 <= self.course <= 6:
            raise ValueError("Course must be between 1 and 6")
        if not 1 <= self.average_score <= 100:
            raise ValueError("Average score must be between 1 and 100")


student_dto = StudentDto(
    first_name="Alice",
    last_name="Smith",
    age=20,
    course=3,
    average_score=85.5
)


