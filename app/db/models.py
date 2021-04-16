from pydantic import BaseModel, Field, EmailStr, BaseConfig


class EmployeeSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0, lt=150)
    company: str = Field(...)
    join_date: str = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(..., gt=0)

    class Config(BaseConfig):
        schema_extra = {
            "example": {
                "name": "First Last",
                "email": "example@test.com",
                "age": 24,
                "company": "Company",
                "join_date": "2021-04-16T15:28:15-08:00",
                "job_title": "Job",
                "gender": "male",
                "salary": 7777
            }
        }
