from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
import database, models, crud, schemas, auth
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(username=user.username, password=auth.fake_hash(user.password))
    db.add(new_user)
    db.commit()
    return {"msg": "user created"}

@app.post("/shorten")
def shorten(url: schemas.URLCreate, db: Session = Depends(get_db)):
    code = crud.gen_code()
    new = models.URL(original_url=url.original_url, short_code=code)
    db.add(new)
    db.commit()
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str, db: Session = Depends(get_db)):
    obj = db.query(models.URL).filter_by(short_code=code).first()
    if not obj:
        raise HTTPException(404)
    obj.clicks += 1
    db.commit()
    return RedirectResponse(obj.original_url)

@app.get("/stats")
def stats(db: Session = Depends(get_db)):
    data = db.query(models.URL).all()
    return data
