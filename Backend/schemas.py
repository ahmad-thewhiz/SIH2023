from typing import List
from pydantic import BaseModel

# base schema for user data
class UserInfoBase(BaseModel):
    username:str
    fullname:str

#schema for user creation(registration)
class UserCreate(UserInfoBase):
    password:str

#inherits from user data schema
class UserInfo(UserInfoBase):
    id:int

    class Config:
        orm_mode = True

#base schema for user login
class UserLogin(BaseModel):
    username:str
    password:str

#base schema for items
class ItemInfo(BaseModel):
    itemname:str
    itemprice:int

#inherits from item data schema used for getting item by id
class ItemAInfo(ItemInfo):
    id:int

    class Config:
        orm_mode = True

#base schema for relating a cart to it's user
class CartOwnerInfo(BaseModel):
    username:str

#base schema for adding items to cart
class CartInfo(BaseModel):
    itemname:str
    itemprice:int

#base schema for getting items in the cart by id
class CartItemAInfo(CartInfo):
    id:int

    class Config:
        orm_mode = True

#base schema for the payment api
class UserPayment(BaseModel):
    phonenumber:int
    total:int
    

class AmazonPrice(BaseModel):
    Title: str
    Price: float
    Rating: float
    URL: str
    ImgURL: str
    
class FlipkartPrice(BaseModel):
    productName: str
    productPrice: str
    productURL: str
    
class IndiamartPrice(BaseModel):
    productName: str
    productURL: str
    productPrice: str

class GeMPrice(BaseModel):
    productName: str
    brandName: str
    lowestPrice: float
    imageURL: str
    
class chatbotInput(BaseModel):
    message: str
    
class chatbotOutput(BaseModel):
    message: str
    response: str