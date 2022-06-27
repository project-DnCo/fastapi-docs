from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


@app.get('/')
def home():
    return {'Data': 'Testing'}


@app.get('/about')
def about():
    return {'Data': 'About'}


inventory = {
    # 1: {
    #     'name': 'Milk',
    #     'price': 3.99,
    #     'brand': 'Regular',
    # },
}


# @app.get('/get-item/{item_id}/{name}')
# def get_item(item_id: int, name: str):
#     return inventory[item_id]


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description='The ID of the item you\'d like to view', gt=0)):
    return inventory[item_id]


@app.get('/get-by-name/{item_id}')
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id, item_data in inventory.items():
        if item_data.name == name:
            return item_data
    # return {'Data': 'Not found'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='Item ID does not exist.')


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {'Error': 'Item ID already exists.'}
        raise HTTPException(status_code=400, detail='Item ID already exists.')
    # inventory[item_id] = {'name': item.name,
    #                       'brand': item.brand, 'price': item.price}
    inventory[item_id] = item
    return inventory[item_id]


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {'Error': 'Item ID does not exist.'}
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description='The ID of the item to delete', gt=0)):
    if item_id not in inventory:
        return {'Error': 'Item ID does not exist.'}
    del inventory[item_id]
    return {'Success': 'Item deleted'}
