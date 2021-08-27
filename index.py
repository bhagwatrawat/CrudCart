import pymongo
import dns
import certifi



def deleteItem(dbname):   # to delete an item from a cart
    collection_name=dbname['items_list']
    cart_name=input("Enter the cart name ")
    query_name = dbname['cart_name']
    items_details1 = query_name.find({'cart_name': cart_name})
    if len(list(items_details1)) == 0:
        print("cart not found ...")
        return
    items_details = collection_name.find({'cart_name': cart_name})
    if items_details.count()==0:
        print("cart is empty")
    item_name= input("Enter the item name ")
    dic={'item_name': item_name,
         }
    x=collection_name.delete_one(dic)
    print("Item is deleted")
    print(x)

def getItems(dbname):
    collection_name=dbname['items_list']
    cart_name= input("Enter the Cart name ")
    query_name=dbname['cart_name']
    items_details1 = query_name.find({'cart_name': cart_name})
    if len(list(items_details1)) == 0:
        print("cart not found ...")
        return
    items_details =collection_name.find({'cart_name':cart_name})
    if items_details.count()==0 :
        print("cart is empty...")
        return
    for item in items_details:
        print(item)
def addItem(dbname):
    collection_name =dbname['items_list']
    cart_name=input("Enter cart name ")
    query_name=dbname['cart_name']
    items_details = query_name.find({'cart_name': cart_name})
    if len(list(items_details)) == 0:
        print("cart not found ... create a cart to add item ")
        return
    item_name=input("Enter item name ")
    price=int(input("Enter item Price "))
    quantity=int(input("Enter quantity "))
    item={
        'cart_name':cart_name,
        'item_name':item_name,
        'item_price':price,
        'quantity':quantity,

    }
    collection_name.insert_one(item)
    print("Item added successfully to cart {}".format(cart_name))

def get_database():

    ca = certifi.where()
    # to create a cart
    client = pymongo.MongoClient("mongodb+srv://bhagwat:admin@cluster0.w2mrx.mongodb.net/cartCrud?retryWrites=true&w=majority", tlsCAFile=ca)
    db = client['cartCrud']
    return db
def createCart(dbname):
    user_name= input("Enter the User Name ")
    cart_name=input("Enter the Cart Name ")
    collection_name = dbname["cart_name"]
    item_1 = {
        "user_name": user_name,
        "cart_name": cart_name
    }
    collection_name.insert_one(item_1)
    print("cart Created Successfully")

if __name__ == "__main__":
    # Get the database
    dbname = get_database()
    while 1:
        print("Enter 1 to create a cart \n Enter 2 to add item inside a cart \n Enter 3 to get the Items from a cart \n Enter 4 to delete item form a cart \n Enter 5 to exit")
        n = int(input())
        if n==1 : createCart(dbname)
        if n==2 : addItem(dbname)
        if n==3 : getItems(dbname)
        if n==4 : deleteItem(dbname)
        if n==5 : exit(0)










