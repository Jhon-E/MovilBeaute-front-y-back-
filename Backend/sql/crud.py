from sqlalchemy.orm import Session
from sql import models, schemas

def get_user_by_email(db: Session, email: str):
    
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    
    db_user = models.User(email=user.email, name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_stylists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stylist).offset(skip).limit(limit).all()

def create_stylist(db: Session, stylist: schemas.StylistCreate):
    
    db_stylist = models.Stylist(email=stylist.email, name=stylist.name, password=stylist.password, profession=stylist.profession)
    db.add(db_stylist)
    db.commit()
    db.refresh(db_stylist)
    return db_stylist
    
def get_stylist_by_email(db: Session, email: str):
        
    return db.query(models.Stylist).filter(models.Stylist.email == email).first()
    
def update_user(db: Session, user: schemas.UserBase, email: str):
    
    db_user = db.query(models.User).filter(models.User.email == email).first()
    
    if db_user:
        for key, value in user.dict().items():
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
    else:
        return {"message": "User not found."}
        
    return db_user

def update_stylist(db: Session, stylist: schemas.StylistBase, email: str):
    
    db_stylist = db.query(models.Stylist).filter(models.Stylist.email == email).first()
    
    if db_stylist:
        for key, value in stylist.dict().items():
                setattr(db_stylist, key, value)

        db.commit()
        db.refresh(db_stylist)
    else:
        return {"message": "User not found."}
        
    return db_stylist