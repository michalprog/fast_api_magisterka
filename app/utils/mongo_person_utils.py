from typing import List, Dict
from app.config.mongo_database import mongo_person_collection
from app.models.statistics import Statistics, UniversalPerson

def get_all() -> List[Dict]:
    docs = list(mongo_person_collection.find())
    for d in docs:
        d["id"] = str(d["_id"])
        d.pop("_id", None)
    return docs

def create_persons(persons: List[Dict]) -> List[Dict]:
    docs = [{k: v for k, v in p.items() if k != "id"} for p in persons]
    result = mongo_person_collection.insert_many(docs)
    for rec, inserted_id in zip(persons, result.inserted_ids):
        rec["id"] = str(inserted_id)
    return persons

def person_statistics() -> List[Statistics]:
    docs = list(mongo_person_collection.find())
    if not docs:
        return []

    persons = []
    for d in docs:
        persons.append({
            "id": str(d["_id"]),
            "name": d.get("name", ""),
            "surname": d.get("surname", ""),
            "salary": d.get("salary", 0),
            "description": d.get("description"),
            "role": d.get("role", 0),
        })

    # grupowanie po roli
    grouped_by_role: Dict[int, List[Dict]] = {}
    for p in persons:
        grouped_by_role.setdefault(p["role"], []).append(p)

    stats: List[Statistics] = []

    # 📌 Statystyki ogólne ("all")
    total_all = sum(p["salary"] for p in persons)
    avg_all = total_all / len(persons)
    min_all = min(persons, key=lambda p: p["salary"])
    max_all = max(persons, key=lambda p: p["salary"])

    stats.append(Statistics(
        role="all",
        count=len(persons),
        averageSalary=avg_all,
        minSalaryPerson=UniversalPerson(
            name=min_all["name"],
            surname=min_all["surname"],
            salary=min_all["salary"],
            role=min_all["role"],
        ),
        maxSalaryPerson=UniversalPerson(
            name=max_all["name"],
            surname=max_all["surname"],
            salary=max_all["salary"],
            role=max_all["role"],
        ),
    ))

    # 📌 Statystyki per rola 0..4
    for role in range(0, 5):
        role_group = grouped_by_role.get(role, [])
        if not role_group:
            continue

        total = sum(p["salary"] for p in role_group)
        avg = total / len(role_group)
        min_p = min(role_group, key=lambda p: p["salary"])
        max_p = max(role_group, key=lambda p: p["salary"])

        stats.append(Statistics(
            role=str(role),
            count=len(role_group),
            averageSalary=avg,
            minSalaryPerson=UniversalPerson(
                name=min_p["name"],
                surname=min_p["surname"],
                salary=min_p["salary"],
                role=min_p["role"],
            ),
            maxSalaryPerson=UniversalPerson(
                name=max_p["name"],
                surname=max_p["surname"],
                salary=max_p["salary"],
                role=max_p["role"],
            ),
        ))

    # 📌 sortowanie – "all" pierwsze
    stats.sort(key=lambda s: (0 if s.role == "all" else int(s.role)))
    return stats
