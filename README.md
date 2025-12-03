

# KARST NETWORKS DATASETS FOR THE ERC-KARST PROJECT

This dataset regroups karst networks survey data provided by cavers and cleaned and saved in specific format for graph analysis and water flow modeling.

We processed and cleaned cave survey data collected by cavers around the world. Cave survey were provided in a variety of format, which we trsnformed to Therion project, and then compiled the Therion project into SQL database. From this SQL database, we regroupe the identical stations, and rename the node ids. We then remove the duplicates and surface points, and add or remove links manually by visual inspection in 3D. When available we collecte conduit cross-sectional geometry (splays or left-right-up-down), or other flags.

## 1. Rights

All the datasets in this repository are under the CC-BY-NC-SA licence. By using those cave datasets, you are acknowledging that:
1. you will always cite and/or thank the cave data owners (information availabe in each data folder (readme))
2. if you share the data, you need to share it under the same conditions, with the appropriate acknowledgement and citation information
3. the data cannot be used for commercial purpose

Note: There is an additional repository containing cave network survey data. KNdata-confidental is a private repository only accessible to the members of the ERC-Karst project, upon request to celia.trunz@unine.ch. If you are not part of this project but are interested in those dataset, you can contact us and we will put you in contact with the data owners.

<!-- The final result is a graph dataset, with a list of edges and nodes attributes. We describe bellow the list of files that can be found for each cave. Not all the files may be present. -->






## 2. Data 

### 2.1 folder architecture
The datasets have been saved in two different folders (caves_fulldatasets and caves_individual). Since some datasets are composed of multiple individual caves we decided to provide both, the clean complete dataset as we received it [(caves_fulldatasets)](https://github.com/ERC-Karst/KNdata-public/tree/main/caves_fulldatasets), and separate files for each cave larger than 500m [(caves_individual)](https://github.com/ERC-Karst/KNdata-public/tree/main/caves_individual).



```bash
KNdata-public
├───caves_fulldatasets
│   ├───data
│   │   └───ID_Cavename_Subset 
│   └───caves_properties_summary.csv
├───caves_individual
│   ├───data
│   │   └───ID_Cavename_Subset 
│   └───caves_properties_summary.csv
├───caves_synthetic
│   ├───data
│   │   └───ID_Cavename_Subset 
│   └───caves_properties_summary.csv
├───notebooks
│   ├───Cavename.sql
│   └───Cavename_corrections.yaml
├───caves_properties_summary_all_fulldatasets.csv
├───caves_properties_summary_all_individual.csv
└───find_your_cave.py
```

<!-- ### 1.1 Full datasets -->
**caves_fulldatasets:** The **full datasets** can contain one or multiple caves. Those caves have been grouped by the caves or caving club in charge of the mapping. Sometimes the caves are combined for practical reason (which has nothing to do with their potential connectivity), for example, Austrian caving club organize their data per map grid cell. Other times the caves are combined because they are suspected to be part of the same network and to eventually connect, as the exploration goes on. Full datasets names end with '000'.

**caves_individual:** The **individual caves** are each one a single connected components. This means that the all the nodes are connected to a unique graph. If the connected component was isolated from a larger file in "caves_fulldatasets", then the number is '001' or larger. If the file name ends with '000' then it means that the fulldataset was already one single connected component.

**caves_properties_summary_all_fulldatasets.csv:** Table containing the list of all the full datasets collected for the ERC-Karst project, with the main statistical values calculated on the datasets, as well as some of the important metadata. 

**caves_properties_summary_all_individual.csv:** Table containing the list of all connected components extracted from the fulldatasets, with the main statistical values calculated on the component, as well as some of the important metadata. 

Note: All the datasets from the project ERC-Karst are listed in the .csv files. In this repository, only the open datasets are available. In the table, all the datasets starting with 'C' are stored in a separate and private github repository (KNdata-public) 

**ID_Cavename_subset:** Naming convention for each dataset. 
- **ID:** Three digit number assigned to each dataset received.
    - if the ID starts with a numeral then the dataset is under open data agreement.
    - if the ID starts with the letter 'C', this means that the data is under a confidential agreement and is stored in the KNdata-confidential repository.
- **Cavename:** Short name assigned to the dataset (usually based on the orginal name of the dataset or cave, or netowrk)
- **Subset** Three digit number assigned to each connected component of a single dataset ID_Cavename. The subset number are organized by size. The smaller the number, the larger the connected component. For instance, the subset 001 will be the largest connected component of the dataset ID_Cavename. Note: full datasets have the subset number '000'

For each dataset (individual or fulldatasets) exist a folder named based on the naming convention and containing the clean files, some visualization files, as well as a metadata file:

```bash
ID_Cavename_Subset
├───ID_Cavename_Subset_metadata.yaml
├───ID_Cavename_Subset.s6
├───ID_Cavename_Subset.yaml
├───clean_graph_csv
│   ├───ID_Cavename_Subset_eges.csv
│   ├───ID_Cavename_Subset_node_pos.csv 
│   └───ID_Cavename_Subset_node_csdim.csv (if available)
├───visualization
│   ├───Cavename.sql
│   └───Cavename_corrections.yaml
└───visualization (add Gocad, and other visualization??)
    ├───ID_Cavename_Subset_clean.3d  
    ├───ID_Cavename_Subset_clean.lox 
    └───ID_Cavename_Subset_shapefiles_clean 
        ├───shot3d.shp
        └───stations3d.shp
    
```
 
<!-- ### Clean data folder content -->
### 2.2 Data formats:

- **sparse6 files** -->`ID_Cavename_Subset.s6`: They only have edges (no position, or any other attributes attached to the edges and nodes). they are usefull for those who want to study the topology only. 

- [**csv files** --> clean_graph_csv](https://github.com/ERC-Karst/KNdata-public/docs/source/clean_csv_files_description.md): This folder contains separate .csv files
    - edges.csv: list of links between the nodes. [from,to]
    - node attributes: list of the nodes with 

- **yaml file** --> `ID_Cavename_Subset.yaml`: They are the most complete clean dataset. They contain edges, edges attributes, node attributes, and metadata, stored in one file. A import function is available in Karstnet-ERC

    - NODES ATTRIBUTES:
        - ['csdim'](https://github.com/ERC-Karst/KNdata-public/docs/source/conduit_geometry.md): list of 2 floats, [Width,Height] in m
        - 'fulladdress': station name and path in the original folder - project
        - 'idsql': station id in the sql database
        - 'pos': list of 3 floats, [easting,northing,elevation], in specific coordinate system
        - 'splays': list of list of 3 floats, [easting,northing,elevation]. each node can have multiple splays
        - 'comments': list of strings.
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
### 2.3 Visualization formats (2D or 3D):



- `Cavename_clean.3d`: 3D visualisation of the clean dataset. .3D is the Aven data format. To visualize the file, install [Survex](https://fileexpert.net/engine/go.php?url=https://survex.com/screenshots.htmlhttps:/) (most simple installation) or [Therion](https://fileexpert.net/engine/go.php?url=https://therion.speleo.sk) (more complex).
- shapefiles
    - `shots3d.shp`: Esri line shapefile 
    - `stations3d.shp`: Esri point shapefile





## 3 How to load the data


### Load the clean datasets in python networkx object with Karstnet

- [import yaml](https://github.com/ERC-Karst/Karstnet-ERC/blob/main/notebooks/Read_and_write_yamlfile_graph.ipynb): Load all or part of the edges and nodes attributes. (!!! add the link)
- [import sparse6]():









