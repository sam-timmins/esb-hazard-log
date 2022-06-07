let map, infoWindow;
let latRef = document.querySelector('#latitude');
let longRef = document.querySelector('#longitude');
let resetTextRef = document.querySelector('#reset-text');
let locationTracker = false;
const getLocationButtonRef = document.querySelector("#get-location");
const resetLocationButtonRef = document.querySelector("#reset-location");
const mapRef = document.querySelector('#map');

window.onload = (event) => {
    mapRef.style.display = 'none';
};

const getHtmlGeolocation = () => {
    locationTracker = true;
    map = new google.maps.Map(mapRef, {
        zoom: 17,
        mapTypeId: 'satellite',
        streetViewControl: false,
    });
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                const marker = new google.maps.Marker({
                    position: pos,
                    map: map,
                });

                latRef.value = position.coords.latitude;
                longRef.value = position.coords.longitude;
                mapRef.style.display = 'block';
                resetTextRef.innerHTML = '';

                map.setCenter(pos);
            },
            () => {
                handleLocationError(true, infoWindow, map.getCenter());
            }
        );
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
};

const initMap = () => {
    infoWindow = new google.maps.InfoWindow();
};

const resetLocation = () => {
    latRef.value = '';
    longRef.value = '';
    if (locationTracker === false) {
        resetTextRef.innerHTML = 'Location has not yet been set';
    } else {
        resetTextRef.innerHTML = 'Your location has been reset';
        mapRef.style.display = 'none';
        locationTracker = false;
    }
};

const handleLocationError = (browserHasGeolocation, infoWindow, pos) => {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
        browserHasGeolocation ?
        "Error: The Geolocation service failed." :
        "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
};

window.initMap = initMap;

getLocationButtonRef.addEventListener('click', getHtmlGeolocation);
resetLocationButtonRef.addEventListener('click', resetLocation);
