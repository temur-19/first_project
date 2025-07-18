class Passenger:
    def __init__(self, passportID: int, fullName: str, gender: str):
        self.passportID = passportID
        self.fullName = fullName
        self.gender = gen  
    def getpassportID(self):
        return self.passportID
    
    def getfullName(self):
        return self.fullName
    
    def getGender(self):
        return self.gender
    
    def __str__(self):
        return f"    PassportID: {self.passportID}\n    FullName: {self.fullName}\n    Gender: {self.gender}"
    
passenger1 = Passenger(12345, "ALi Aliyev", "Male")
passenger2 = Passenger(54321, "Aziz Azizov", "Male")
passenger3 = Passenger(77777, "Azizbek Aliyev", "Male")
passenger4 = Passenger(67890, "Ali Azizov", "Male")



class Driver:
    def __init__(self, passportID: int, fullName: str, age:int):
        self.passportID = passportID
        self.fullName = fullName
        self.age = age
    
    def getpassportID(self):
        return self.passportID
    
    def getfullName(self):
        return self.fullName
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return f"\n   PassportID: {self.passportID}\n   FullName: {self.fullName}\n   Age: {self.age}"

driver1 = Driver(6789, "Temur Xasanov", 20)



class Train:
    def __init__(self, trainID:int, name: str, speed: int, driver: Driver):
        self.trainID = trainID
        self.name = name
        self.speed = speed
        self.driver = driver

    def gettrainID(self):
        return self.trainID

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def __str__(self):
        return f"\n   TrainID: {self.trainID}\n   Name: {self.name}\n   Speed: {self.speed} km/h\nDriver:{self.driver}"
Train1 = Train(919191, "UZtrain", 300, driver1)        
Train2 = Train(191919, "Uztrain", 300, driver1)



class Platform:
    def __init__(self, platformID: int, status: str):
        self.platformID = platformID
        self.status = status
        
    def getplatformID(self):
        return self.platformID
    
    def getStatus(self):
        return self.status
    
    def __str__(self):
        return f"\n    PlatformID: {self.platformID}\n    Status: {self.status}"

platform1 = Platform(111111, "Online")
platform2 = Platform(222222, "Online")


class Trip:
    def __init__(self, From:str, to: str, train: Train, platform: Platform, Passengers:list,  priceTrip: int, dateTrip: str):
        self.From = From
        self.to = to
        self.train = train
        self.platform = platform
        self.Passengers = Passengers
        self.priceTrip = priceTrip
        self.datetrip = dateTrip

    def getFrom(self):
        return self.From
    
    def getTo(self):
        return self.to
    
    def getPassengers(self,):
        my_text = f"Passengers:\n"
        for index, passenger in enumerate(self.Passengers, 1):
            my_text+=f"{index}\n{passenger}\n"
        return my_text
    
    def getPriceTrip(self):
        return self.priceTrip
    
    def getDateTrip(self):
        return self.datetrip
    
    def __str__(self):
        return f"From: {self.From}\nTo: {self.to}\nTrain: {self.train}\nPlatform: {self.platform}\n {self.getPassengers()}PriceTrip: {self.priceTrip} $\nDatetrip: {self.datetrip}"

trip1 = Trip("Toshkent", "Samarqand", Train1, platform1,[passenger1, passenger2], 70, "20.07.2025")
trip2 = Trip("Samarqand", "Shahrisabz", Train2, platform2,[passenger3,passenger4], 70, "20.07.2025")



class RailwayStation:
    def __init__(self, name: str, address: str, Trip: list):
        self.name = name
        self.address = address
        self.Trip = Trip
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getTrip(self):
        my_text1=f""
        for index, trip in enumerate(self.Trip,1):
            my_text1+=f"Trip{index}:\n{trip}\n   "
        return my_text1

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\n {self.getTrip()}"
    
Rw1 = RailwayStation("Toshkent temir yo'l vokzali", "Toshkent",  [trip1])
Rw2 = RailwayStation("Samarqand temir yo' vokzali", "Samarqand", [trip2])
print(Rw1)
print(Rw2)


