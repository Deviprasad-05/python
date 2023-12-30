class bookMyShow:
    def _init_(self):
        self.available_seets=100
        self.booking={}
    def book_tickets(self,name,num_tickets,selected_seets):
        if num_tickets <= self.available_sets:
               print("booking {num_tickets},ticket for {name}...")
        self.available_seets-=num_tickets
        self.booking[name]={"Tickets":num_tickets,"slected_seets":selected_seets}
    print("tickets boocked successfully.(self.available_seets)seets remaining.")
# book my show
def main():
     name=input('enter your name:- ')
     tickets=int(input("enter the number of seets:-"))
     seets=input("enter your selected seets:-")
#book seets
     tickets(user_nae,num_tickets,seets)
