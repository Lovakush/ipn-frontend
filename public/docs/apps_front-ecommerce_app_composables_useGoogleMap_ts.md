# useGoogleMap.ts

**Path**: `apps\front-ecommerce\app\composables\useGoogleMap.ts`

## Summary
=================================
HOW TO USE GOOGLE MAP COMPOSABLE
=================================

1 - In &lt;PARENT&gt; component script setup, get &amp; install the GMap script
@example
```ts
const { installGMapScripts } = useGoogleMap()
installGMapScripts()
```

2 - If you want to use a google autocomplete input,
use the component &lt;Geolocator&gt; with a &lt;IGeolocator&gt; v-model.
You can bind the disabled&lt;boolean&gt; v-model to manage the loading state
You can overwrite the filters slot under the search input
@example
```ts
&lt;Geolocator
v-model="geoLocatedLookup"
v-model:disabled="disabled"
search-label="LABEL ABOVE SEARCH INPUT"
search-placeholder="PLACEHOLDER INSIDE SEARCH INPUT"
default-value="Default address"
/&gt;
```

3 - If you want to use a toggle button to display either the map or the list,
use the component &lt;GoogleMapDisplayType&gt; with a &lt;"list" | "map"&gt; v-model.
You can use the disabled&lt;boolean&gt; prop to manage the disabled state
@example
```ts
&lt;GoogleMapDisplayType
v-model="mapDisplayMode"
:disabled="disabled"
/&gt;
```

4 - If you want to display the list of places,
use the component &lt;GoogleMapListing&gt; with a selected place&lt;IMarker | undefined&gt; as v-model.
You can use the places &lt;IMarker[]&gt; prop to set the list of places
You can use the disabled&lt;boolean&gt; prop to manage the disabled state
You can overwrite the card by setting some slots (images/details/tags)
@example
```ts
&lt;GoogleMapListing
v-model="place"
:places="places"
:disabled="disabled"
/&gt;
```

5 - If yo want to display the map with some markers corresponding to the places,
use the component &lt;GoogleMapContainer&gt; with a selected &lt;Marker&gt; as v-model.
You also need to give an array of places &lt;IMarker[]&gt; and a function
&lt;marker-info-content-builder&gt; that return a string template
to display an InfoContent while a marker is clicked
You can use the disabled&lt;boolean&gt; prop to manage the disabled state
@example
```ts
&lt;GoogleMapContainer
v-model="CurrentSelecterMarker"
:places="markers"
:marker-info-content-builder="markerInfoContentBuilder"
:disabled="disabled"
/&gt;
```

## Function Details

### `useGoogleMap`


### `getContentSVG`

- **Parameters**: `place: IMarker`

### `loadGMapLibraries`


### `installGMapScripts`


