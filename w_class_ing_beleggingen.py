#28-11-2021
import pandas as pd

class ING_Portfolio():
    """Super Class ING Portfolio. Contains <p_df> dataframe with all assets per portfolio.
    Has got following wokring variables inside the class: 
        p_val (float) : total value.
        p_prof (float) : total unrealised profit.
        p_a_types (list) : different types of investments (grouped dataframe).
    Args:
        p_cur (str) : Currency of the portfolio.
        p_debug (boolean) : Debug mode for the class.
    Returns:
        <none> 
    """
    def __init__(self, w_cur, w_debug : bool) -> None:
        self.p_df = pd.DataFrame()
        self.p_cur = w_cur
        self.p_debug = w_debug
        self.p_val, self.p_prof = float(0), float (0)
        self.p_a_types = []

    def __repr__(self) -> str:
        """Returns a string summary of the portfolio when print(self) is called.
        Args:
            <none>
        Returns:
            <string> : Reponse string with value & unreleased profit. Provides asset category details when available.
        """
        response = f"=> ING Portfolio contains {len(self.p_df)} share assets, alltogether valued at: {self.p_val:,.0f} {self.p_cur}, including an unrealised profit of: {self.p_prof:,.0f} {self.p_cur}."
        if self.p_a_types != [] : 
            for a_df in self.p_a_types:
                df_as_str = f"  - {a_df[['Assetcategorie']].values[0]} ({a_df[['Verdeling %']].values[0]:,.0f}%): {a_df[['Huidige waarde EUR']].values[0]:,.0f} {self.p_cur}, including an unrealised profit of: {a_df[['Ongerealiseerd rendement EUR']].values[0]:,.0f} {self.p_cur}."
                response += f"\n{str(df_as_str)}"
        return(response)
    
    def analyse_groups(self):
        #would like to be able to sort by values as well.
        self.p_a_types=[]
        g_df = self.p_df.groupby('Assetcategorie')
        #g_df.sort_values(['Huidige waarde EUR'], ascending=False, inplace=True)
        for a_cat, w_group in g_df:
            w_group = w_group[['Huidige waarde EUR','Verdeling %', 'Kostprijs EUR', 'Ongerealiseerd rendement EUR']].sum()
            #w_group = w_group.sort_values(['Huidige waarde EUR'], ascending=False)
            w_group['Assetcategorie'] = a_cat
            self.p_a_types.append(w_group)

    def calc_unrealised_profit(self) -> None:
        """Calculates the unrealised profit.
        """
        print(f"===> Calculating unrealised profit.")
        self.p_prof = float(0)
        for index, row in self.p_df.iterrows():
            self.p_prof += float(row["Ongerealiseerd rendement EUR"])

    def find_pos(self, w_largest: bool, w_absolute: bool, w_number: int) -> pd.DataFrame:
        """Function to find the <x> largest/smallest positions, either by absolute value or percentage.

        Args:
            w_largest (bool): <True> for largest position, <False> for smallest.
            w_absolute (bool):<True> for absolute position, <False> for %.
            w_number (int): Number of positions to return.

        Returns:
            pd.DataFrame: Returns a DataFrame.
        """
        if w_absolute == True :
            w_df = self.p_df.sort_values(['Huidige waarde EUR'], ascending=not(w_largest)).head(w_number)
        else :
            w_df = self.p_df.sort_values(['Verdeling %'], ascending=not(w_largest)).head(w_number)
        return(w_df)
    
    def find_roi(self, w_best: bool, w_absolute: bool, w_number: int) -> pd.DataFrame:
        """Function to find the <x> number of best/worst performing assets, either by absolute value or percentage.

        Args:
            w_best (bool): <True> for best performing ROI, <False> for worst.
            w_absolute (bool): <True> for absolute ROI, <False> for %.
            w_number (int): Number of positions to return.

        Returns:
            pd.DataFrame: Returns a DataFrame.
        """
        if w_absolute == True :
            w_df = self.p_df.sort_values(['Ongerealiseerd rendement EUR'], ascending=not(w_best)).head(w_number)
        else :
            w_df = self.p_df.sort_values(['Ongerealiseerd rendement %'], ascending=not(w_best)).head(w_number)
        return(w_df)
      
    def load_portfolio_file (self, w_path) -> None:
        """Loads the ING portfolio file into the class.
        Changes the number format to <float> with '.' as decimal seperation.
        
        Args:
            w_path (pathlib): File system path to be loaded.
        """
        self.p_df = pd.read_csv (w_path, delimiter=';', quotechar='"', encoding='cp1252')     
        #convert the file to the normal float standards
        self.p_df["Huidige waarde EUR"] = self.p_df["Huidige waarde EUR"].replace(r'\,',r'.', regex=True) 
        self.p_df["Huidige waarde EUR"] = self.p_df["Huidige waarde EUR"].astype(float)
        self.p_df["Positie"] = self.p_df["Positie"].replace(r'\,',r'.', regex=True) 
        self.p_df["Positie"] = self.p_df["Positie"].astype(float)
        self.p_df["Koers"] = self.p_df["Koers"].replace(r'\,',r'.', regex=True) 
        self.p_df["Koers"] = self.p_df["Koers"].astype(float)
        self.p_df["Verdeling %"] = self.p_df["Verdeling %"].replace(r'\,',r'.', regex=True) 
        self.p_df["Verdeling %"] = self.p_df["Verdeling %"].astype(float)
        self.p_df["Kostprijs EUR"] = self.p_df["Kostprijs EUR"].replace(r'\,',r'.', regex=True) 
        self.p_df["Kostprijs EUR"] = self.p_df["Kostprijs EUR"].astype(float)
        self.p_df["Ongerealiseerd rendement EUR"] = self.p_df["Ongerealiseerd rendement EUR"].replace(r'\,',r'.', regex=True) 
        self.p_df["Ongerealiseerd rendement EUR"] = self.p_df["Ongerealiseerd rendement EUR"].astype(float)
        self.p_df["Ongerealiseerd rendement %"] = self.p_df["Ongerealiseerd rendement %"].replace(r'\,',r'.', regex=True) 
        self.p_df["Ongerealiseerd rendement %"] = self.p_df["Ongerealiseerd rendement %"].astype(float)
        if self.p_debug == True : print(self.p_df)
    
    def print_det_port (self) -> None:
        """Print all holdings in the self.pd_df in full. Uses class __repr__(self).
        """
        print(self)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 25)
        print (self.p_df)
        #pd.reset_option('all') 
    
    def value_portfolio (self) -> None:
        """Values the portfolio in <p_val> variable.
        """
        print(f"===> Calculating portfolio value.")
        self.p_val = float(0)
        for index, row in self.p_df.iterrows():
            self.p_val += float(row["Huidige waarde EUR"])
        
        