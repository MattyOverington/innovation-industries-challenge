import datetime as dt
from os import error, rename, path
from urllib.parse import urlencode
from typing import List
import requests
from fastapi import APIRouter, Depends  # Body,
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import config, models, utils, schemas


router = APIRouter()


@router.get("/jobs", response_model=List[models.Job])
def get_jobs(*, db: Session = Depends(utils.get_db)):
    jobs = db.query(schemas.Job).all()
    return jobs
    


@router.get("/job", response_model=models.Job)
def get_job(*, db: Session = Depends(utils.get_db), id: int):
    job = db.query(schemas.Job).filter(schemas.Job.id == id).first()
    return job


@router.post("/job", response_model=models.Job)
def create_job(
    *,
    db: Session = Depends(utils.get_db),
    job: models.Job
):
    job_data = job.dict(exclude_unset=True)
    db_job = schemas.Job(**job_data)
    db.add(db_job)
    db.commit()
    
    return db_job


@router.delete("/job")
def delete_milestone_type_ref(
    *, db: Session = Depends(utils.get_db), id: int
):
    db.query(schemas.Job).filter(schemas.Job.id == id).delete()
    db.commit()
