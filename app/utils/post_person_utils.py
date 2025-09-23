from typing import List, Dict
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.repo.post_person_repository import PostPersonRepository
from app.models.statistics import Statistics, UniversalPerson

def get_all() -> List[Dict]:
    with SessionLocal() as db:
        persons = db.query(PostPersonRepository).all()
        return [
            {
                "id": p.id,
                "name": p.name,
                "surname": p.surname,
                "salary": p.salary,
                "description": p.description,
                "role": p.role,
                "active": getattr(p, "active", True),  # jeśli masz w modelu
            }
            for p in persons
        ]

def create_persons(persons: List[Dict]) -> List[Dict]:
    created = []
    with SessionLocal() as db:
        for person in persons:
            new_p = PostPersonRepository(
                name=person["name"],
                surname=person["surname"],
                salary=person["salary"],
                description=person.get("description"),
                role=person["role"],
            )
            db.add(new_p)
            db.commit()
            db.refresh(new_p)

            created.append({
                "id": new_p.id,
                "name": new_p.name,
                "surname": new_p.surname,
                "salary": new_p.salary,
                "description": new_p.description,
                "role": new_p.role,
                "active": getattr(new_p, "active", True),
            })
    return created

def person_statistics() -> List[Statistics]:
    with SessionLocal() as db:
        persons = db.query(PostPersonRepository).all()
        if not persons:
            return []

        # grupowanie po roli
        grouped_by_role: Dict[int, List[PostPersonRepository]] = {}
        for p in persons:
            grouped_by_role.setdefault(p.role, []).append(p)

        stats: List[Statistics] = []

        # 📌 Statystyki ogólne ("all")
        total_all = sum(p.salary for p in persons)
        avg_all = total_all / len(persons)
        min_all = min(persons, key=lambda p: p.salary)
        max_all = max(persons, key=lambda p: p.salary)

        stats.append(Statistics(
            role="all",
            count=len(persons),
            averageSalary=avg_all,
            minSalaryPerson=UniversalPerson(
                name=min_all.name,
                surname=min_all.surname,
                salary=min_all.salary,
                role=min_all.role,
            ),
            maxSalaryPerson=UniversalPerson(
                name=max_all.name,
                surname=max_all.surname,
                salary=max_all.salary,
                role=max_all.role,
            ),
        ))

        # 📌 Statystyki per rola 0..4
        for role in range(0, 5):
            role_group = grouped_by_role.get(role, [])
            if not role_group:
                continue

            total = sum(p.salary for p in role_group)
            avg = total / len(role_group)
            min_p = min(role_group, key=lambda p: p.salary)
            max_p = max(role_group, key=lambda p: p.salary)

            stats.append(Statistics(
                role=str(role),
                count=len(role_group),
                averageSalary=avg,
                minSalaryPerson=UniversalPerson(
                    name=min_p.name,
                    surname=min_p.surname,
                    salary=min_p.salary,
                    role=min_p.role,
                ),
                maxSalaryPerson=UniversalPerson(
                    name=max_p.name,
                    surname=max_p.surname,
                    salary=max_p.salary,
                    role=max_p.role,
                ),
            ))

        # 📌 sortowanie – "all" pierwsze
        stats.sort(key=lambda s: (0 if s.role == "all" else int(s.role)))
        return stats
