import uvicorn
from typing import List

from fastapi import FastAPI

from app.db.app import get_employees_by_filter
from app.db.models import EmployeeSchema

app = FastAPI()


@app.get(
    "/employees/{filters}", response_description="List all employees"
)
async def get_employees_data_by_filter(
        filters: str,
        query: str,
        comparison: str = None,  # gt, lt, eq, lte, gte
        extra_for_compare: str = None  # use when comparison = gt or gte; $lt: extra_for_compare

) -> List[EmployeeSchema]:
    employees = await get_employees_by_filter(filters, query, comparison, extra_for_compare)
    return employees


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
