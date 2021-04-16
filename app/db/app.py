import os
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from .models import EmployeeSchema


client = AsyncIOMotorClient(os.environ["DB_PATH"])
db = client.test


async def get_employees_by_filter(
        filters: str,
        query: str,
        comparison: str = None,
        extra_for_compare: str = None
        ) -> List[EmployeeSchema]:

    if filters in ("age", "salary"):
        if comparison is not None:
            if extra_for_compare is not None:
                query = {f"$gt": int(query), f"$lt": int(extra_for_compare)}
            else:
                query = {f"${comparison}": int(query)}
        else:
            query = int(query)

    employees: List[EmployeeSchema] = []
    rows = db["employees"].find({filters: query})

    async for row in rows:
        employees.append(
            EmployeeSchema(**row)
        )
    return employees
