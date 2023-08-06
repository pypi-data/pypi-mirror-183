""" 
Assess Model
- Used for assessing 
"""


from datetime import date
from pydantic import BaseModel, EmailStr,root_validator,validator
from typing import List, Optional,Union
from datetime import date
from base.models.commonmodel import CommonModel
from base.models.educationbase import EducationBase,EducationHistory
from base.models.employmentbase import EmploymentBase
from base.models.employmenthistory import EmploymentHistory
from base.models.language import LanguageBase,Languages
from base.models.utils import makeList

class Personal(BaseModel):
    last_name: str
    first_name: str
    native_last_name:str
    native_first_name:str
    sex: str
    dob: date
    email:Optional[EmailStr]
    

class Status(BaseModel):
    current_country:str
    current_country_status:str
    current_workpermit_type:Optional[str]
    has_vr:Optional[bool]

class Language(LanguageBase):
    pass 
    
class Assumption(BaseModel):
    job_title:str
    noc_code:str
    hourly_rate:float
    city:str	
    province:str	
    start_date:date	
    end_date:date
    work_permit_type:str
    
class Education(EducationBase):
    is_trade:bool
    academic_year:float
    graduate_date:date
    city:str
    province:str
    country:str
    
class Employment(EmploymentBase):
    employment_type:str	 # self-employed or employed	
    company:str	
    city:Optional[str] 
    province:Optional[str]
    country:str
    share_percentage:float
    work_under_status:Optional[str]
    duties:List[str]
    
    _normalize_duties = validator("duties", allow_reuse=True, pre=True)(makeList)
    
    
    """ 
    1. if country is Canada:
    - province and city is must; otherwise, it's optional.
    - work_under_status is must
    
    """
    @root_validator(pre=True)
    def validate_canada(cls, values):
        if values["country"].upper() == "CANADA":
            if values["province"] is None or values["province"] not in  [
            "AB",
            "BC",
            "MB",
            "NB",
            "NL",
            "NS",
            "NT",
            "NU",
            "ON",
            "PE",
            "QC",
            "SK",
            "YT",
        ]:
                raise ValueError("Province is missing or mis-spelled since the country is Canada")
            if values["city"] is None:
                raise ValueError("City is required since the country is Canada")
            if values["work_under_status"] is None:
                raise ValueError("Work under status is required since the country is Canada")
        return values
    
    
class CanadaRelative(BaseModel):
    last_name:str
    first_name:str
    relationship:str
    status:str
    age:int	
    province:str
    years_in_canada:int
        
class AssessModel(BaseModel):
    personal: Personal
    status:Status
    language:List[Language]
    assumption:List[Assumption]
    education:List[Education]
    employment:List[Employment]
    canadarelative:List[CanadaRelative]
    

class AssessModelE(CommonModel, AssessModel):
    def __init__(self, excels=None, output_excel_file=None, language=None):
        from base.models.utils import excel_language_path

        path = excel_language_path(language)
        mother_excels = [path + "/pa.xlsx"]
        super().__init__(
            excels, output_excel_file, mother_excels, globals(), language=language
        )

