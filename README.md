

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

### 2.1 Folder architecture
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
- **caves_fulldatasets:** The **full datasets** can contain one or multiple caves. Those caves have been grouped by the caves or caving club in charge of the mapping. Sometimes the caves are combined for practical reason (which has nothing to do with their potential connectivity), for example, Austrian caving club organize their data per map grid cell. Other times the caves are combined because they are suspected to be part of the same network and to eventually connect, as the exploration goes on. Full datasets names end with '000'.

- **caves_individual:** The **individual caves** are each one a single connected components. This means that the all the nodes are connected to a unique graph. If the connected component was isolated from a larger file in "caves_fulldatasets", then the number is '001' or larger. If the file name ends with '000' then it means that the fulldataset was already one single connected component.

- **caves_properties_summary_all_fulldatasets.csv:** Table containing the list of all the full datasets collected for the ERC-Karst project, with the main statistical values calculated on the datasets, as well as some of the important metadata. 

- **caves_properties_summary_all_individual.csv:** Table containing the list of all connected components extracted from the fulldatasets, with the main statistical values calculated on the component, as well as some of the important metadata. 

Note: All the datasets from the project ERC-Karst are listed in the .csv files. In this repository, only the open datasets are available. In the table, all the datasets starting with 'C' are stored in a separate and private github repository (KNdata-public) 

### 2.2 ID_Cavename_subset:

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

- [**csv files** --> clean_graph_csv](https://github.com/ERC-Karst/KNdata-public/blob/main/docs/source/clean_csv_files_description.md): This folder contains separate .csv files
    - `ID_Cavename_Subset_edges.csv`: list of links between the nodes. ``[ID_from,ID_to]``
    - `ID_Cavename_Subset_node_pos`: list of the nodes ID with x,y,z coordinates. `[ID,x,y,z]`
    - `ID_Cavename_Subset_node_csdim`: list of the nodes ID with cross-sectional width dimension. ``[ID,CS_height,CS_width]``

- **yaml file** --> `ID_Cavename_Subset.yaml`: They are the most complete clean dataset. They contain edges, edges attributes, node attributes, and metadata, stored in one file. A import function is available in Karstnet-ERC

    - NODES ATTRIBUTES:
        - ['**csdim**'](https://github.com/ERC-Karst/KNdata-public/blob/main/docs/source/conduit_geometry.md): list of 2 floats, ``[Width,Height]`` in m
        - '**pos**': list of 3 floats, ``[easting,northing,elevation]``, in specific coordinate system
        - '**splays**': list of list of 3 floats, ``[easting,northing,elevation]``. each node can have multiple splays
        - '**comments**': list of strings.
        - '**flags**': list of strings. (see appendix below)
        - '**fulladdress**': station name and path in the original folder - project
        - '**idsql**': station id in the sql database

    - EDGES ATTRIBUTES:
        - '**comments**': list of strings.
        - '**flags**': list of strings. (see appendix below)

### 2.3 Visualization formats (2D or 3D):



**Aven files**:

- `Cavename_clean.3d`: 3D visualisation of the edges and nodes
- `Cavename_clean.lox`: 3D visualisation of the volumes (if conduite dimensions are available)

Note: To visualize the .3d and .lox files, install [Survex](https://fileexpert.net/engine/go.php?url=https://survex.com/screenshots.htmlhttps:/) (most simple installation) or [Therion](https://fileexpert.net/engine/go.php?url=https://therion.speleo.sk) (more complex).

**ESRI shapefiles**:
- `shots3d.shp`: Esri line shapefile of the edges
- `stations3d.shp`: Esri point shapefile of the nodes


Note: the `.S6`, `.csv`, or `.yaml` can be imported in python (usually as a Networkx object) and plotted in 2D or 3D. [Karsnet-ERC](https://github.com/ERC-Karst/Karstnet-ERC) contains such functions. 



## 3 How to load the data in Python 


### 3.1 Load the clean datasets in python networkx object with Karstnet

- [import yaml](https://github.com/ERC-Karst/Karstnet-ERC/blob/main/notebooks/Read_and_write_yamlfile_graph.ipynb): Load all or part of the edges and nodes attributes. 
- [import sparse6](): 


---
Appendix
---

Node flags:
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

Edge flags:
- `dpl`: duplicate
- `srf`: surface
- `art`: artificial

## Cave list

 **id** | short name | total length [m]| total depth [m]| csdim [%]| n° CC | mean degree | country | license
|---|---|---|---|---|---|---|---|---|
| **001** | GouffreDejaVu | 150 | 32.16 | 100 | 1 | 1.5 | Chile | CC BY-NC-SA 4.0 |
| **002** | Migovec | 46317 | 968.62 | 13 | 1 | 2.09 | Slovenia | CC BY-NC-SA 4.0 |
| **003** | Criou | 31680 | 1669.43 | 28 | 20 | 2.02 | France | CC BY-NC-SA 4.0 |
| **004** | Matienzo | 378972 | 843.0 | 1 | 583 | 1.97 | Spain | CC BY-NC-SA 4.0 |
| **005** | Sakany | 6846 | 140.71 | 94 | 12 | 2.19 | France | CC BY-NC-SA 4.0 |
| **006** | ReveEveille | 330 | 124.5 | 98 | 1 | 1.5 | Chile | CC BY-NC-SA 4.0 |
| **007** | Tsanfleuron | 9124 | 667.71 | 99 | 29 | 1.82 | Switzerland | CC BY-NC-SA 4.0 |
| **008** | UltimaPatagonia | 38755 | 693.51 | 16 | 101 | 1.92 | Chile | CC BY-NC-SA 4.0 |
| **009** | Folly | 85481 | 1890.82 | 10 | 131 | 1.96 | France | CC BY-NC-SA 4.0 |
| **010** | PlaninaPoljana | 25221 | 1144.61 | 89 | 96 | 1.93 | Slovenia | CC BY-NC-SA 4.0 |
| **011** | BreznoNaToscu | 1870 | 581.27 | 90 | 1 | 1.95 | Slovenia | CC BY-NC-SA 4.0 |
| **012** | Pokljuskega Grebena | 13364 | 762.25 | 77 | 3 | 2.07 | Slovenia | CC BY-NC-SA 4.0 |
| **013** | BurringtonCombe | 5334 | 91.04 | 32 | 15 | 2.17 | UK | CC BY-NC-SA 4.0 |
| **014** | CheddarCatchment | 27414 | 289.55 | 49 | 54 | 2.05 | UK | CC BY-NC-SA 4.0 |
| **015** | CountyClare | 76613 | 292.5 | 13 | 51 | 2.03 | Ireland | CC BY-NC-SA 4.0 |
| **016** | CountyMayo | 3792 | 73.3 | 61 | 9 | 2.09 | Ireland | CC BY-NC-SA 4.0 |
| **017** | LittleNeathRiver | 8633 | 122.43 | 0 | 2 | 2.24 | UK | CC BY-NC-SA 4.0 |
| **018** | Lathkill | 5099 | 156.0 | 0 | 7 | 1.94 | UK | CC BY-NC-SA 4.0 |
| **019** | Loser | 356868 | 1238.01 | 4 | 259 | 2.17 | Austria | TBD |
| **020** | Vanoise | 2592 | 438.06 | 84 | 11 | 2.05 | France | CC BY-NC-SA 4.0 |
| **021** | Glacier | 4411 | 230.47 | 100 | 1 | 2.38 | Switzerland | CC BY-NC-SA 4.0 |
| **022** | CombeBryon | 4198 | 644.16 | 99 | 1 | 2.27 | Switzerland | CC BY-NC-SA 4.0 |
| **023** | Charbonniere | 116 | 23.72 | 100 | 1 | 1.5 | Switzerland | CC BY-NC-SA 4.0 |
| **024** | Lajoux | 1305 | 220.16 | 95 | 1 | 1.97 | Switzerland | CC BY-NC-SA 4.0 |
| **026** | PuitsWilly | 110 | 73.51 | 96 | 1 | 1.5 | Switzerland | CC BY-NC-SA 4.0 |
| **027** | CreuxDEntier | 1397 | 151.84 | 100 | 1 | 2.15 | Switzerland | CC BY-NC-SA 4.0 |
| **028** | NarinesBoeuf | 700 | 116.72 | 97 | 1 | 2.06 | Switzerland | CC BY-NC-SA 4.0 |
| **029** | RougeEau | 655 | 131.06 | 98 | 1 | 1.94 | Switzerland | CC BY-NC-SA 4.0 |
| **031** | DYO | 16385 | 123.46 | 0 | 1 | 2.02 | UK | CC BY-NC-SA 4.0 |
| **032** | FermanagAndCavan | 1231 | 65.09 | 83 | 1 | 2.06 | Ireland | TBD |
| **033** | WestKingsdale | 12698 | 166.08 | 1 | 13 | 2.04 | UK | CC BY-NC-SA 4.0 |
| **035** | EastKingsdale | 1035 | 131.24 | 0 | 2 | 1.91 | UK | CC BY-NC-SA 4.0 |
| **036** | ShkembejtJames | 2808 | 532.54 | 0 | 7 | 1.52 | Albania | TBD |
| **037** | FountainsFell | 8039 | 198.18 | 0 | 8 | 2.01 | UK | CC BY-NC-SA 4.0 |
| **038** | Ingleborough | 7789 | 226.35 | 10 | 12 | 1.86 | UK | CC BY-NC-SA 4.0 |
| **039** | DunaldMill | 260 | 24.0 | 0 | 1 | 1.78 | UK | CC BY-NC-SA 4.0 |
| **040** | Nidderdale | 5173 | 90.54 | 80 | 6 | 2.14 | UK | CC BY-NC-SA 4.0 |
| **041** | ThreeCounties | 90323 | 251.22 | 0 | 39 | 2.12 | UK | CC BY-NC-SA 4.0 |
| **042** | DowProv | 2621 | 75.14 | 0 | 1 | 2.0 | UK | CC BY-NC-SA 4.0 |
| **043** | HaggBeck | 3222 | 108.84 | 0 | 5 | 2.0 | UK | CC BY-NC-SA 4.0 |
| **047** | Seefeldhoele | 2240 | 35.71 | 100 | 1 | 2.78 | Switzerland | CC BY-NC-SA 4.0 |
| **048** | Banquier | 12838 | 196.36 | 17 | 1 | 2.17 | France | CC BY-NC-SA 4.0 |
| **049** | Cochon | 4286 | 178.49 | 0 | 1 | 2.06 | France | CC BY-NC-SA 4.0 |
| **050** | Andara | 64773 | 1826.22 | 33 | 83 | 1.99 | Spain | CC BY-NC-SA 4.0 |
| **054** | Koytendag | 19527 | 1194.9 | 82 | 20 | 2.14 | Turkmenistan | CC BY-NC-SA 4.0 |
| **055** | Tatra | 5476 | 330.37 | 18 | 5 | 1.95 | Poland | CC BY-NC-SA 4.0 |
| **056** | ClydachGorge | 3197 | 153.04 | 0 | 3 | 1.86 | UK | CC BY-NC-SA 4.0 |
| **058** | Cavernicole | 2654 | 356.2 | 89 | 1 | 2.06 | France | CC BY-NC-SA 4.0 |
| **059** | FontaineNoire | 827 | 62.73 | 55 | 2 | 2.12 | France | CC BY-NC-SA 4.0 |
| **060** | ClotAspres | 38258 | 1134.58 | 5 | 15 | 2.07 | France | CC BY-NC-SA 4.0 |
| **061** | Moucherotte | 10016 | 843.29 | 0 | 14 | 2.06 | France | CC BY-NC-SA 4.0 |
| **062** | Sornin | 46877 | 1337.32 | 32 | 12 | 2.13 | France | CC BY-NC-SA 4.0 |
| **063** | Perthuis | 2264 | 368.34 | 19 | 4 | 1.93 | France | CC BY-NC-SA 4.0 |
| **066** | Blau | 1336 | 106.93 | 0 | 1 | 1.92 | France | CC BY-NC-SA 4.0 |
| **067** | Bailleurs | 2138 | 120.47 | 0 | 1 | 2.01 | France | CC BY-NC-SA 4.0 |
| **068** | Mandra | 844 | 94.49 | 0 | 1 | 2.0 | France | CC BY-NC-SA 4.0 |
| **069** | Argent | 527 | 23.97 | 0 | 1 | 2.0 | France | CC BY-NC |
| **070** | Cheminee | 6364 | 395.14 | 0 | 1 | 2.13 | France | CC BY-NC-SA 4.0 |
| **071** | Carcabon | 12957 | 212.96 | 79 | 1 | 1.99 | Spain |  |
| **073** | Serreno | 4777 | 179.8 | 5 | 1 | 2.08 | Spain |  |
| **074** | Yeux | 1312 | 263.75 | 30 | 1 | 1.97 | Spain |  |
| **075** | TorcaAitken | 9031 | 271.44 | 0 | 1 | 2.04 | Spain |  |
| **076** | CuevaCarrera | 8490 | 143.75 | 15 | 1 | 2.06 | Spain |  |
| **077** | Pasillo | 5462 | 276.16 | 4 | 1 | 2.04 | Spain |  |
| **079** | CuevaPollita | 2461 | 87.18 | 78 | 1 | 2.13 | Spain |  |
| **080** | Lastrias | 1756 | 144.26 | 74 | 1 | 1.9 | Spain |  |
| **082** | CuevaTonia | 2112 | 170.14 | 84 | 1 | 1.94 | Spain |  |
| **083** | Cubillo | 6536 | 141.31 | 3 | 1 | 2.02 | Spain |  |
| **084** | CuevaHelguera | 2650 | 173.81 | 19 | 1 | 2.0 | Spain |  |
| **085** | Requiem | 2524 | 331.25 | 0 | 1 | 1.89 | Spain |  |
| **087** | CoumeBere | 1734 | 473.34 | 75 | 1 | 1.94 | France |  |
| **088** | PerteYerse | 1640 | 399.27 | 14 | 1 | 1.95 | France |  |
| **089** | Queou | 4769 | 457.65 | 41 | 1 | 2.04 | France |  |
| **090** | Crolles | 45539 | 693.92 | 92 | 26 | 2.13 | France | CC BY-NC-SA 4.0 |
| **091** | Som | 3343 | 937.0 | 91 | 7 | 1.87 | France | CC BY-NC-SA 4.0 |
| **092** | Flaine | 2216 | 906.0 | 29 | 8 | 1.88 | France | CC BY-NC-SA 4.0 |
| **093** | Larra | 333773 | 2016.0 | 2 | 377 | 1.94 | France | CC BY-NC-SA 4.0 |
| **095** | Kelmend | 3594 | 1459.6 | 17 | 16 | 1.79 | Albania |  |
| **C001** | Poteu | 5517 | 323.42 | 99 | 1 | 2.25 | Switzerland | Private dataset|
| **C002** | FeesVD | 36318 | 227.41 | 99 | 1 | 2.31 | Switzerland | Proprietary dataset|
| **C003** | FeesVS | 3561 | 253.81 | 100 | 1 | 2.18 | Switzerland | Proprietary dataset|
| **C004** | GrandCor | 4753 | 589.85 | 99 | 1 | 2.05 | Switzerland | Proprietary dataset|
| **C005** | Bouillon | 3794 | 24.7 | 0 | 1 | 2.15 | France | TBD |
| **C006** | DiableRouge | 265 | 37.31 | 100 | 1 | 2.0 | France | TBD |
| **C007** | Escargots | 681 | 73.81 | 90 | 2 | 2.11 | France | TBD |
| **C009** | Espelugues | 237 | 16.82 | 97 | 1 | 2.0 | France | TBD |
| **C010** | Sarrazins | 687 | 31.41 | 96 | 2 | 1.93 | France | TBD |
| **C012** | Labastide | 1507 | 87.39 | 97 | 1 | 2.21 | France | TBD |
| **C013** | Monachou | 673 | 32.64 | 94 | 1 | 2.2 | France | TBD |
| **C014** | Bedat | 1633 | 103.15 | 96 | 1 | 2.14 | France | TBD |
| **C015** | Cardal | 884 | 71.5 | 95 | 1 | 2.29 | France | TBD |
| **C016** | Loup | 560 | 64.51 | 95 | 2 | 1.76 | France | TBD |
| **C017** | PicDuJer | 613 | 67.74 | 95 | 1 | 2.07 | France | TBD |
| **C018** | Tunnel | 920 | 31.29 | 98 | 1 | 2.15 | France | TBD |
| **C019** | Maraichers | 72 | 14.87 | 93 | 1 | 1.5 | France | TBD |
| **C021** | Carbonniere | 2665 | 134.21 | 84 | 1 | 2.12 | France | TBD |
| **C022** | RoyReineFou | 5032 | 334.38 | 83 | 10 | 2.0 | France | TBD |
| **C027** | Shuanghe | 134751 | 767.0 | 95 | 43 | 2.0 | China | TBD |
| **C028** | OxBelHa | 370057 | 61.57 | 0 | 1 | 2.46 | Mexico | Proprietary dataset|
| **C029** | Longirod | 5151 | 518.32 | 98 | 1 | 2.04 | Switzerland | Proprietary dataset|
| **C031** | Baerwies | 7459 | 361.02 | 1 | 1 | 2.11 | Austria | Proprietary dataset|
| **C032** | DachsteinMammutHoehle | 69878 | 1207.58 | 11 | 1 | 2.12 | Austria | Proprietary dataset|
| **C033** | Hirschgruben | 5919 | 201.02 | 31 | 1 | 2.09 | Austria | Proprietary dataset|
| **C034** | Steinbockschacht | 2876 | 1126.39 | 0 | 1 | 2.11 | Austria | Proprietary dataset|
| **C035** | TrockenesLoch | 4495 | 108.52 | 0 | 1 | 2.1 | Austria | Proprietary dataset|
| **C036** | Arphidia | 13528 | 635.19 | 96 | 2 | 2.22 | France | TBD |
| **C037** | Vallorbe | 6759 | 128.28 | 90 | 5 | 2.19 | Switzerland | Proprietary dataset|
| **C038** | Covatannaz | 5159 | 104.17 | 98 | 2 | 2.09 | Switzerland | Proprietary dataset|
| **C039** | BlueSpringIndiana | 33628 | 14.92 | 0 | 1 | 2.25 | USA | Proprietary dataset|
| **C040** | BlueSpringTennessee | 50780 | 74.55 | 0 | 1 | 2.24 | USA | Proprietary dataset|
| **C042** | AgenAllwedd | 13651 | 122.62 | 0 | 1 | 2.05 | UK | Proprietary dataset|
| **C045** | Ceberi | 7175 | 310.77 | 95 | 4 | 2.08 | France | TBD |
| **C047** | Krubera | 13233 | 2191.0 | 0 | 1 | 2.06 | Georgia | TBD |
| **C049** | EglwysFaen | 1340 | 18.65 | 0 | 1 | 2.06 | UK | Proprietary dataset|
| **C050** | DarenCilau | 19951 | 186.15 | 0 | 1 | 2.13 | UK | Proprietary dataset|
| **C055** | Crevice | 4908 | 0.0 | 0 | 1 | 2.07 | USA | TBD |
| **C056** | Crossroads | 7781 | 0.0 | 0 | 1 | 2.32 | USA | TBD |
| **C058** | Jewel | 355242 | 223.83 | 88 | 515 | 2.0 | USA | Proprietary dataset|
| **C059** | Fulfords | 1645 | 79.78 | 0 | 3 | 2.28 | USA | CC BY-NC-SA 4.0 |
| **C060** | Tonion | 16397 | 580.2 | 0 | 1 | 2.15 | Austria | Proprietary dataset|
| **C061** | Burgunder | 23503 | 560.71 | 62 | 1 | 2.1 | Austria | Proprietary dataset|
| **C063** | Wind | 271709 | 191.69 | 0 | 1 | 2.28 | USA | Proprietary dataset|
| **C064** | Lechugilla | 261889 | 484.91 | 79 | 1 | 2.44 | USA | Proprietary dataset|
| **C068** | CuevaGuerta | 24011 | 289.52 | 91 | 1 | 2.22 | Spain | TBD |
| **C069** | HohlaubA1A3 | 1681 | 280.11 | 98 | 1 | 2.1 | Switzerland | Proprietary dataset|
| **C070** | HohlaubG3 | 1405 | 219.35 | 99 | 1 | 2.04 | Switzerland | Proprietary dataset|
| **C071** | SacActun | 356871 | 162.82 | 0 | 26 | 2.04 | Mexico | Proprietary dataset|
| **C072** | Duerrenstein32 | 5196 | 472.99 | 0 | 1 | 2.1 | Austria | Proprietary dataset|
| **C073** | Duerrenstein211 | 1289 | 248.7 | 0 | 1 | 2.08 | Austria | Proprietary dataset|
| **C074** | Duerrenstein273 | 1271 | 133.42 | 0 | 1 | 2.12 | Austria | Proprietary dataset|
| **C075** | FoussoubieEvent | 2624 | 29.86 | 97 | 1 | 2.08 | France | Proprietary dataset |
| **C076** | FoussoubieGoule | 20379 | 40.79 | 98 | 1 | 2.29 | France | Proprietary dataset |
| **C077** | Kanine | 125743 | 1965.64 | 45 | 71 | 1.98 | Slovenia | CC BY-NC-SA 4.0 |
