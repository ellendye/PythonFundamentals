class Store:
    product_list = []
    def __init__(self,store_name):
        self.store_name = store_name

    def add_product(self,new_product):
        #takes a product and adds it to the store

        self.new_product = Product(name=new_product, price=input("Price? "), category=input("Category? "))
        product_id = len(self.product_list)
        self.product_list.append([[f'Product: {self.new_product.name}'], [f'Price: ${self.new_product.price}'], [f'Category: {self.new_product.category}'], [f'ID: {product_id}']])
        print("New product: ")
        self.new_product.print_info(product_id)
        return self
    def sell_product(self,id):
        #removes product from the store's list of products given the id(assume id is the index) and print it's info
        print(f"product sold: {self.product_list[id]}")
        self.product_list[id] = []
        return self
    def inflation(self,percent_increase):
        #increases the price of each product by percent increase given (use the method you wrote in the product class)
        self.new_product.update_price(percent_change=percent_increase,is_increased=True)
        return self
    def set_clearance(self,category,percent_discount):
        #updates all of the products matching the given category by reducing the price by percent given(use the method written in product class)
        self.new_product.update_price(percent_change=percent_discount,is_increased=False)
        return self


class Product():
    def __init__(self,name,price,category):
        self.name = name
        self.price = int(price)
        self.category = category
    def update_price(self,percent_change,is_increased):
        #updates the products price. if is_increased is True, price should icrease by percent_change provided. If False, should decrease by percent_change provided
        if is_increased:
            for product in range(len(Store.product_list)):
                if len(Store.product_list[product]) > 0:
                    Store.product_list[product][1] = percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self,id):
        #name of product, it's category and it's price
        print (f"Product name: {self.name} Price is ${self.price} Category: {self.category} Store ID: {id}")
        return self


broccoli = Product('broccoli',5,'vegetable')
store = Store('Dojo Store')
store.add_product(broccoli)