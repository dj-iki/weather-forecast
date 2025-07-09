from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.update_log import UpdateLog
from ..utils.logger import logger


def get__daily_update_log(db: Session):
    update_log = db.query(UpdateLog).filter(UpdateLog.data_type == 'daily').first()

    if update_log:
        return update_log
    else:
        logger.error("")

def get__hourly_update_log(db: Session) -> UpdateLog:
    update_log = db.query(UpdateLog).filter(UpdateLog.data_type == 'hourly').first()

    if update_log:
        return update_log
    else:
        logger.error("")

def update__daily_update_log(db: Session):
    update_log = db.query(UpdateLog).filter(UpdateLog.data_type == 'daily').first()

    if update_log:
        update_log.last_updated = func.now() 
        db.commit()
        logger.info("Daily update log updated seccessfully")
    else:
        logger.error("Daily update log entry is missing in the 'update_log' table.")



def update__hourly_update_log(db: Session):
    update_log = db.query(UpdateLog).filter(UpdateLog.data_type == 'hourly').first()

    if update_log:
        update_log.last_updated = func.now()
        db.commit
        logger.info("Hourly update log updated seccessfully")
    else:
        logger.error("Hourly update log entry is missing in the 'update_log' table.")