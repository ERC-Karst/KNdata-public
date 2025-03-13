# KARST NETWORKS DATASETS FOR THE ERC-KARST PROJECT

This dataset regroups karst networks graph data.

We processed and cleaned cave survey data collected by cavers around the world. Cave survey were provided in a variety of format, which we trsnformed to Therion project, and then compiled the Therion project into SQL database. From this SQL database, we regroupe the identical stations, and rename the node ids. We then remove the duplicates and surface points, and add or remove links manually by visual inspection in 3D. When available we collecte conduit cross-sectional geometry (splays or left-right-up-down), or other flags.

The final result is a graph dataset, with a list of edges and nodes attributes. We describe bellow the list of files that can be found for each cave. Not all the files may be present.


## Load the clean datasets in python networkx object with Karstnet

- [import csv](): Load all or part of the edges and nodes attributes. (!!! add the link)
- [import yaml](): Load all or part of the edges and nodes attributes. (!!! add the link)
- [import sparse6]():

## To load the original dataset (without cleaning)

- [import therion sql enhanced]() (!!! add the link)


## Data folder architecture

The clean cave network graph data is stored in the [data](https://github.com/ERC-Karst/KNdata-public/tree/main/data) folder, where ach subfolder is a network (ID_Cavename):

```bash
ID_Cavename
├───metadata.yaml
├───clean_data
│   ├───Cavename.s6
│   ├───Cavename.yaml
│   └───clean_graph_csv
│       ├───Cavename_edges.csv
│       ├───Cavename_edges_flags.csv (optional)
│       ├───Cavename_edges_comments.csv (optional)
│       ├───Cavename_node_pos.csv
│       ├───Cavename_node_fulladdress.csv
│       ├───Cavename_node_idsql.csv
│       ├───Cavename_node_csdim.csv (optional)
│       ├───Cavename_node_splays.csv (optional)
│       ├───Cavename_node_flags.csv (optional)
│       └───Cavename_node_comments.csv (optional)
├───sql_database
│   ├───Cavename.sql
│   └───Cavename_corrections.yaml
└───visualization (add Gocad, and other visualization??)
    ├───Cavename_clean.3d   
    └───Cavename_clean.lox  
    todo: shapefile (with clean data)




```
 
### Clean data folder content
- **sparse6 file:** only edges (no position, or any other attributes attached to the edges and nodes)
- **yaml file:** edges, edges attributes, node attributes, metadata, stored in one file
- [**csv files:**](https://github.com/ERC-Karst/KNdata-public/docs/source/clean_csv_files_description.md) edges, edges attributes, node attributes, metadata, are each stored in a separate file. 

### SQL database
Contains the original database stored in a sql format created with Therion, and optionally the correction file when necessary.

### Visualization folder
<!-- - `shots3d.shp`: Esri line shapefile 
- `stations3d.shp`: Esri point shapefile -->
- `Cavename_clean.3d`: 3D visualisation of the clean dataset. .3D is the Aven data format. To visualize the file, install [Survex](https://fileexpert.net/engine/go.php?url=https://survex.com/screenshots.htmlhttps:/) (most simple installation) or [Therion](https://fileexpert.net/engine/go.php?url=https://therion.speleo.sk) (more complex).


### List of dictionnaries attached to the graph:
- NODES ATTRIBUTES:
    - ['csdim'](https://github.com/ERC-Karst/KNdata-public/docs/source/conduit_geometry.md): list of 2 floats, [Width,Height] in m
    - 'fulladdress': station name and path in the original folder - project
    - 'idsql': station id in the sql database
    - 'pos': list of 3 floats, [easting,northing,elevation], in specific coordinate system
    - 'splays': list of list of 3 floats, [easting,northing,elevation]. each node can have multiple splays
    - 'flags': list of strings.
        - `ent`: entrance, points where the cave intersect with the surface
        - `con` : continuation, cavers identified this last point of a survey session as potentially leading futher
        - `inl`: inlet, points with water input from a un-surveyed side passage (note: will be displayed in sketch)
        - `oul`: outlet, points with water output towards a un-surveyed side passage (note: will be displayed in sketch)
        - `fix`: fixed
        - `spr` : spring 
        - `sin`: sink, position inside or at the end of a passage where water is exiting through the ground or the wall.
        - `dol`: doline 
        - `dig` : dig
        - `air` : air-draught 
        - `ove` : overhang 
        - `arc` : arch attributes
        - `waf`: position at the top or inside a wall where water can or is falling
        - `smp`: sump
        - `str`: position where a stream is present in the conduit
- EDGES ATTRIBUTES:
    - 'comments': list of strings.
    - 'flags': list of strings.
        - `dpl`: duplicate
        - `srf`: surface
        - `art`: artificial








