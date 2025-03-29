Object subclass: Ride [
    | rideID pickupLocation dropoffLocation distance fare |

    Ride >> initialize: id pickup: pickup dropoff: dropoff distance: dist [
        rideID := id.
        pickupLocation := pickup.
        dropoffLocation := dropoff.
        distance := dist.
        fare := 0.
    ]

    Ride >> fareCalculation [
        fare := distance * 1.0.
        ^fare
    ]

    Ride >> rideDetails [
        'Ride ID: ', rideID displayNl.
        'Pickup: ', pickupLocation, ', Dropoff: ', dropoffLocation displayNl.
        'Distance: ', distance displayString displayNl.
        'Fare: $', self fareCalculation displayString displayNl.
    ]
]

Ride subclass: StandardRide [
    StandardRide >> fareCalculation [
        fare := distance * 1.5.
        ^fare
    ]
]

Ride subclass: PremiumRide [
    PremiumRide >> fareCalculation [
        fare := distance * 2.0. 
        ^fare
    ]
]

Object subclass: Driver [
    | driverID name rating assignedRides |

    Driver >> initialize: id name: n rating: r [
        driverID := id.
        name := n.
        rating := r.
        assignedRides := OrderedCollection new.
    ]

    Driver >> addRide: ride [
        assignedRides add: ride.
    ]

    Driver >> getDriverInfo [
        'Driver ID: ', driverID displayNl.
        'Name: ', name displayNl.
        'Rating: ', rating displayString displayNl.
        'Assigned Rides: ', assignedRides size displayString displayNl.
    ]

    Driver >> getDriverRides [
        assignedRides do: [:ride | ride rideDetails].
    ]
]

Object subclass: Rider [
    | riderID name requestedRides |

    Rider >> initialize: id name: n [
        riderID := id.
        name := n.
        requestedRides := OrderedCollection new.
    ]

    Rider >> requestRide: ride [
        requestedRides add: ride.
    ]

    Rider >> viewRides [
        'Rider: ', name displayNl.
        'Requested Rides: ', requestedRides size displayString displayNl.
        requestedRides do: [:ride | ride rideDetails].
    ]
]


| ride1 ride2 driver1 driver2 rider |

ride1 := StandardRide new initialize: 'R123' pickup: 'A' dropoff: 'B' distance: 10.
ride2 := PremiumRide new initialize: 'R124' pickup: 'C' dropoff: 'D' distance: 5.

driver1 := Driver new initialize: 'D1' name: 'John Doe' rating: 4.7.
driver2 := Driver new initialize: 'D2' name: 'Jane' rating: 5.
rider := Rider new initialize: 'R001' name: 'Jane Smith'.

driver1 addRide: ride1.
driver2 addRide: ride2.

rider requestRide: ride1.
rider requestRide: ride2.

driver1 getDriverInfo.
'--------------------' displayNl.
driver1 getDriverRides.
'--------------------' displayNl.
driver2 getDriverInfo.
'--------------------' displayNl.
driver2 getDriverRides.
'--------------------' displayNl.
rider viewRides.
