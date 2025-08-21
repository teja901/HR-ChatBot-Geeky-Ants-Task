from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data_loader import EMPLOYEES


model = SentenceTransformer("all-MiniLM-L6-v2")


documents = [
    f"{emp.name}, skills: {', '.join(emp.skills)}, "
    f"experience: {emp.experience_years} years, "
    f"projects: {', '.join(emp.projects)}, "
    f"availability: {emp.availability}"
    for emp in EMPLOYEES
]


embeddings = model.encode(documents, convert_to_numpy=True)


dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search_employees(query: str, top_k: int = 3):
   
    q_emb = model.encode([query], convert_to_numpy=True)
    
   
    distances, indices = index.search(q_emb, top_k)
    
    
    results = []
    for idx in indices[0]:
        emp = EMPLOYEES[idx]
        results.append({
            "name": emp.name,
            "skills": emp.skills,
            "experience": emp.experience_years,
            "projects": emp.projects,
            "availability": emp.availability,
        })
    return results
