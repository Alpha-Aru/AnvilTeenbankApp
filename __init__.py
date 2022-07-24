from ._anvil_designer import money_details_pageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Module1

class money_details_page(money_details_pageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    #This page shows a more detailed 
    
    #Use server side function to generate a list of relevant numbers
    x = list(anvil.server.call('count'))
    print (x)
    
    #Display current income
    self.label_3.text = f"${int(x[5])}"
    #Remove from list
    x.pop(5)
    
    #Display Savings
    self.label_7.text = f"${int(x[5])}"
    saving =  int(x[5] / 7)
    #Remove from List
    x.pop(5)
    
    #Plotly Pie Chart
    self.labels = ["Transport", "Shopping", "Eating Out", "Entertainment","Groceries"]
    self.plot_1.data = go.Pie(labels = self.labels, values = x)
    
    #Calculate Predictions
    self.label_12.text = f"${int(saving * 19)}"
    self.label_13.text = f"${int(saving * 43)}"
    self.label_14.text = f"${int(saving * 67)}"
    
    #Gain Last Month's Data and Do Same Process as Above
    x = list(anvil.server.call('count_month'))
    
    self.label_3_copy.text = f"${x[5]}"
    self.label_5.text = f"${int((sum(x) - x[5]) / 31)}"
    
    daily = int((sum(x) - x[5]) / 31)
    
    self.label_21.text = f"${int(saving * 13)}"
    self.label_22.text = f"${int(saving * 16)}"
    self.label_23.text = f"${int(saving * 19)}"
    
    #Generate Insights
    self.label_8_copy.text = f"This month, you spent ${daily} per day, this is ${(int((sum(x) - x[5])/31) - int(Module1.daily_spending))} lower than your yearly average" 
    self.label_16.text = f"This month, you saved ${x[5]}, this is ${(int(Module1.s_permonth) - int(x[5])) * -1} higher than your yearly average" 
    
    #Plotly Pie Chart
    self.labels = ["Transport", "Shopping", "Eating Out", "Entertainment","Groceries"]
    x.pop(5)
    self.plot_2.data = go.Pie(labels = self.labels, values = x)
    
  #buttons
  def button_1_click(self, **event_args):
    self.card_1.visible = True
    self.button_1.visible = False
    self.yearly_hide.visible = True

  def button_2_click(self, **event_args):
    self.card_1_copy.visible = True
    self.button_2.visible = False
    self.monthly_hide.visible = True

  def monthly_hide_click(self, **event_args):
    self.card_1_copy.visible = False
    self.button_2.visible = True
    self.monthly_hide.visible = False

  def yearly_hide_click(self, **event_args):
    self.card_1.visible = False
    self.button_1.visible = True
    self.yearly_hide.visible = False

  def button_3_click(self, **event_args):
    open_form('money_dashboard')





