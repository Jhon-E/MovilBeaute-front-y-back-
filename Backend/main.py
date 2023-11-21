from fastapi import FastAPI, Depends, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sql.database import SessionLocal, engine
from sql import models, schemas
from json.decoder import JSONDecodeError
import json
from sqlalchemy.orm import Session
from sql import crud
app = FastAPI()
from pydantic import EmailStr
from fastapi.templating import Jinja2Templates

# Agregar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],  # Puedes especificar los métodos permitidos
    allow_headers=["*"],  # Puedes especificar los encabezados permitidos
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/create_user_form")
async def form_create_user(request: Request, db: Session = Depends(get_db)):
    entity = await request.json()
    print("Contenido del JSON recibido:", entity)
    db_user = schemas.UserCreate(email=entity["email"], name=entity["name"], password=entity["password"])
    return create_user(db=db, user=db_user)
    

@app.post("/createuser")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/getusers")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@app.post("/validUser")
async def valid_user(request: Request, db: Session = Depends(get_db)):
    print(1)
    try:
        print(2)
        entity = await request.json()
        print(entity)
        db_user = crud.get_user_by_email(db=db, email=entity["email"])
        db_stylist = crud.get_stylist_by_email(db=db, email=entity["email"])
        print(3)
        if db_user:
            print(4)
            if entity["password"] == db_user.password:
                print(5)
                print("Redirigiendo a http://localhost:5173/inicio")
                return ""
            else:
                print(6)
                raise HTTPException(status_code=400, detail="Contraseña incorrecta.")
        if db_stylist:
            print(7)
            if entity["password"] == db_stylist.password:
                print(8)
                return RedirectResponse(url="http://localhost:5173/inicio", status_code=303)
            else:
                print(9)
                raise HTTPException(status_code=400, detail="Contraseña incorrecta.")
        else:
            raise HTTPException(status_code=400, detail="El usuario no existe.")
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON in request body")

@app.put("/updatestylist")
def update_stylist(email: EmailStr, user: schemas.UserBase, db: Session = Depends(get_db)):
    
    return crud.update_user(db=db, user=user, email=email)

@app.get("/getstylists")
def get_stylists(db: Session = Depends(get_db)):
    return crud.get_stylists(db=db)

@app.post("/createstylist")
def create_stylist(stylist: schemas.StylistCreate, db: Session = Depends(get_db)):
    return crud.create_stylist(db=db, stylist=stylist)

@app.put("/updatestylist")
def update_stylist(email: EmailStr, stylist: schemas.Stylist, db: Session = Depends(get_db)):
    return crud.update_stylist(db=db, stylist=stylist, email=email)
