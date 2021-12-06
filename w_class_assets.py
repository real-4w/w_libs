#7/12/2021 - do not develop here, go w_ing_asset_class
class Asset:
    """Super class for assets. Contains <quantity>, <price>, <value> and <asset_cu> per asset.
    
    Args:
        quantity (float)
        price (float)
        value (float)
        cur (str)
    Returns:
        <none> 
    """
    def __init__(self, a_quantity: float, a_price:float, a_value: float, a_cur: str) -> None:
        self.quantity = a_quantity
        self.price = a_price
        self.value = a_value
        self.cur = a_cur
 
class Crypto(Asset):
    """Class for Crypto Assets, based on Asset Class.

    Args:
        quantity (float): From <Asset> Class
        price (float): From <Asset> Class
        value (float): From <Asset> Class
        cur (str): From <Asset> Class
        name (str): Crypto currency name
        description (str): Description of Crypto currency
    Returns:
        <none> 
        
    """
    def __init__(self, a_quantity: float, a_price: float, a_value: float, a_cur: str, c_name: str, c_description: str) -> None:
        super().__init__(a_quantity, a_price, a_value, a_cur)
        self.name = c_name
        self.description = c_description
        
    def __repr__(self) -> str:
        """Returns a string summary of the crypto asset when print(self) is called."""
        return(f"{self.name:5} : {self.quantity:6.2f} @ {self.price:10,.2f} {self.cur} = {self.value:10,.2f} {self.cur}")

class Property(Asset):
    """Class for Property Assets, based on Asset Class.

    Args:
        quantity (float): From <Asset> Class
        price (float): From <Asset> Class
        value (float): From <Asset> Class
        cur (str): From <Asset> Class
        p_address (str)
        p_description (str)
    """
    def __init__(self, a_quantity: float, a_price, a_value: float, a_cur, p_address, p_description: str, p_mortgage: float) -> None:
        super().__init__(a_quantity, a_price, a_value, a_cur)
        self.address = p_address
        self.description = p_description
        self.mortgage = p_mortgage
    
    def __repr__(self) -> str:
        """Returns a string summary of the property asset when print(self) is called."""
        return(f"{self.address:16} : {self.quantity:,d} value @ {self.price:,d} {self.cur} - {self.mortgage:,d} {self.cur} = {self.value:,d} {self.cur}")

class Shares(Asset):
    """Class for Share Assets, based on Asset Class.

    Args:
        quantity (float): From <Asset> Class
        price (float): From <Asset> Class
        value (float): From <Asset> Class
        cur (str): From <Asset> Class
    """
    def __init__(self, a_quantity, a_price, a_value: float, a_cur, s_name, s_market: str) -> None:
        super().__init__(a_quantity, a_price, a_value, a_cur)
        self.name = s_name
        self.market = s_market

    def __repr__(self) -> str:
        """Returns a string summary of the shares asset when print(self) is called."""
        return(f"{self.market:4}{self.name:4} : {self.quantity:.6f} @ {self.price:.6f} {self.cur} = {str(self.value):11} {self.cur}")

class Portfolio():
    """Portfolio class.

    Args:
        w_cur (string): Current of the portfolio.
        w_debug (bool): Toggle's debugging to see what is going on inside the class.
    """
    def __init__(self, w_cur, w_debug : bool) -> None:
        self.crypto_list, self.property_list, self.share_list = [], [], []
        self.c_tot_val, self.p_tot_val, self.s_tot_val, self.tot_val = float(0), float(0), float(0), float(0) 
        self.port_cur = w_cur
        self.p_debug = w_debug
        
    def __repr__(self) -> str:
        """Returns a string summary of the portfolio when print(self) is called."""
        return(f"===> Portfolio contains {len(self.share_list)} share assets, {len(self.crypto_list)} crypto assets and {len(self.property_list)} property assets, alltogether valued at: {self.tot_val:,.0f} {self.port_cur}")
        
    def add_crypto_asset(self, c_asset: Crypto) :
        """Adds a Crypto(Asset) to the crypto_list in the <Portfolio> Class. Prints the Crypto(Asset) that was added using __repr__(self).

        Args:
            self (Porfolio): Portfolio instance we are working on.
            c_asset (Crypto): Asset to be added to the <crypto_list>.
        """
        self.crypto_list.append(c_asset)
        print (f"Added crypto asset: {c_asset} to portfolio.")

    def add_property_asset(self, p_asset: Property):
        """[summary]

        Args:
            self (Porfolio): Portfolio instance we are working on.
            p_asset (Property): Asset to be added to the <property_list>.
        """
        self.property_list.append(p_asset)
        print (f"Added property asset: {p_asset} to portfolio.")
    
    def add_share_assets(self, s_asset):
        pass

    def calc_port_val (self) :
        print(f"===> Calculating portfolio value.")
        self.c_tot_val, self.p_tot_val, self.s_tot_val, self.tot_val = float(0), float(0), float(0), float(0) 
        #self.tot_val = float(0)
        for c_asset in self.crypto_list: 
            self.c_tot_val += c_asset.value
            if self.p_debug : print (f"Updated portfolio with {c_asset.value:,.0f} {self.p_cur} to {self.tot_val:,.0f} {self.port_cur}") 
        self.tot_val += self.c_tot_val
        for p_asset in self.property_list:
            self.p_tot_val += p_asset.value
            if self.p_debug : print (f"Updated portfolio with {p_asset.value:,.0f} {self.p_cur} to {self.tot_val:,.0f} {self.port_cur}") 
        self.tot_val += self.p_tot_val
    
    def print_all(self) -> None:
        """Method to print all assets in Portfolio Class. Calls __repr__() to get summary before iterating through all Asset Lists in the Asset Class.
        Returns:
            <none> 
        """
        print(self)
        self.print_crypto()
        self.print_share()
        self.print_property()
  
    def print_crypto(self) -> None:
        """Method to print all crypto assets in Portfolio Class.
        Returns:
            <none> 
        """
        print(f"===> Portfolio contains {len(self.crypto_list)} crypto assets valued at: {self.c_tot_val:,.0f} {self.port_cur}")
        for c_asset in self.crypto_list: print (c_asset)            # uses __repr__ from Crypto class.
    
    def print_share(self) -> None:
        """Method to print all crypto assets in Portfolio Class.
        Returns:
            <none> 
        """
        print(f"===> Portfolio contains {len(self.share_list)} share assets valued at: {self.s_tot_val:,.0f} {self.port_cur}")
        for s_asset in self.share_list: print (s_asset)             # uses __repr__ from Share class.
    
    def print_property(self) -> None:
        """Method to print all crypto assets in Portfolio Class.
        Returns:
            <none> 
        """
        print(f"===> Portfolio contains {len(self.property_list)} property assets valued at: {self.p_tot_val:,.0f} {self.port_cur}")
        for p_asset in self.property_list: print (p_asset)          # uses __repr__ from Share class.

