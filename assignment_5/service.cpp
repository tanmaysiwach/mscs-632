#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Ride {
protected:
    string rideID; // uuid
    string pickupLocation; // gps coordinates (?) or text address 
    string dropoffLocation; // gps coordinates (?) or text address
    double distance; 
    double fare;

public:
    Ride(string id, string pickup, string dropoff, double dist)
        : rideID(id), pickupLocation(pickup), dropoffLocation(dropoff), distance(dist), fare(0) {}

    virtual double fareCalculation() {
        fare = distance * 1;
        return fare;
    }

    virtual void rideDetails() {
        cout << "Ride ID: " << rideID << endl;
        cout << "Pickup: " << pickupLocation << ", Dropoff: " << dropoffLocation << endl;
        cout << "Distance: " << distance << " miles" << endl;
        cout << "Fare: $" << fareCalculation() << endl;
    }
};

class StandardRide : public Ride {
public:
    StandardRide(string id, string pickup, string dropoff, double dist)
        : Ride(id, pickup, dropoff, dist) {}

    double fareCalculation() override {
        fare = distance * 1.5;
        return fare;
    }
};

class PremiumRide : public Ride {
public:
    PremiumRide(string id, string pickup, string dropoff, double dist)
        : Ride(id, pickup, dropoff, dist) {}

    double fareCalculation() override { 
        fare = distance * 2.0;
        return fare;
    }
};

class Driver {
private:
    string driverID;
    string name;
    float rating;
    vector<Ride*> assignedRides;

public:
    Driver(string id, string n, float r) : driverID(id), name(n), rating(r) {}

    void addRide(Ride* ride) {
        assignedRides.push_back(ride);
    }

    void getDriverInfo() {
        cout << "Driver ID: " << driverID << ", Name: " << name << ", Rating: " << rating << endl;
        cout << "Assigned Rides: " << assignedRides.size() << endl;
    }

    void getDriverRides() {
        for (auto ride : assignedRides) {
            ride->rideDetails();
        }
    }
};

// Rider Class
class Rider {
private:
    string riderID;
    string name;
    vector<Ride*> requestedRides;

public:
    Rider(string id, string n) : riderID(id), name(n) {}

    void requestRide(Ride* ride) {
        requestedRides.push_back(ride);
    }

    void viewRides() {
        cout << "Rider: " << name << ", Requested Rides: " << requestedRides.size() << endl;
        for (auto ride : requestedRides) {
            ride->rideDetails();
        }
    }
};

int main() {
    Ride* ride1 = new StandardRide("R123", "A", "B", 10);
    Ride* ride2 = new PremiumRide("R124", "C", "D", 5);
    

    Driver driver1("D1", "John Doe", 4.7);
    Driver driver2("D2", "Jane Doe", 4.5);
    Rider rider("R1", "Jane Smith");
    
    driver1.addRide(ride1);
    driver2.addRide(ride2);

    rider.requestRide(ride1);
    rider.requestRide(ride2);

    driver1.getDriverInfo();
    driver1.getDriverRides();
    driver2.getDriverInfo();
    driver2.getDriverRides();
    rider.viewRides();

    delete ride1;
    delete ride2;

    return 0;
}
