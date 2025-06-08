# utils.py

import json


def get_experiences_data_json(work_experiences):
    experiences_data = []
    for exp in work_experiences:
        experiences_data.append(
            {
                "id": exp.id,
                "company": exp.company_name,
                "position": exp.role,
                "period": f"{exp.start_date.strftime('%Y')} - {(exp.end_date.strftime('%Y') if exp.end_date else 'Present')}",
                "location": exp.location,
                "description": list(exp.items.values_list("description", flat=True)),
                "technologies": list(exp.tech_stacks.values_list("name", flat=True)),
            }
        )
    return json.dumps(experiences_data)
