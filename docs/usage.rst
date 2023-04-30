=====
Usage
=====

To use pydeck-grid in a project::

    import os
    import pydeck as pdk
    import xarray as xr
    from pydeck_grid import PcolorLayer

    data = xr.open_dataset(os.path.join(pdk.__file__, "data", "gfs_test.nc"))

    view = pdk.ViewState(
        longitude=float(data.longitude.mean()),
        latitude=float(data.latitude.mean()),
        zoom=3,
        min_zoom=2,
        max_zoom=10,
        pitch=0,
        bearing=0,
    )

    datakeys = {
        "x": "longitude",
        "y": "latitude",
        "u": "UGRD_10maboveground",
        "v": "VGRD_10maboveground",
    }

    layer = PcolorLayer(
        data,
        datakeys,
        id="test",
        colormap="turbo",
        vmin=0,
        vmax=50,
        scale=1.92,
        pickable=True,
        precision=2,
    )
    
    r = pdk.Deck(
        layer,
        initial_view_state=view,
        tooltip={
            "html": "<b>Windspeed:</b> {value} kts",
            "style": {"backgroundColor": "steelblue", "color": "white"},
        },
    )
    
    fname = tempfile.mktemp(suffix=".html")
    r.to_html(fname, True)



