

## Clean database file description

### `*_edge.csv`

All the links between the nodes, after the cleaning process. Referes to the local node ID.


| Column | Name | Type | Units | Description                     |
| -------- | ------ | ------ | ------- | --------------------------------- |
| 1      | from | int  | -     | local node ID of edge departure |
| 2      | to   | int  | -     | local node ID of edge arrival   |

<!-- ### `*_edge_flags.csv`


| Column | Name  | Type                    | Units | Description                                 |
| -------- | ------- | ------------------------- | ------- | --------------------------------------------- |
| 1      | from  | int                     | -     | local node ID of edge departure             |
| 2      | to    | int                     | -     | local node ID of edge arrival               |
| 3      | flags | string, list of strings | -     | any flags that can be attached to the edges |

### `*_edge_comments.csv`


| Column | Name     | Type                    | Units | Description                                    |
| -------- | ---------- | ------------------------- | ------- | ------------------------------------------------ |
| 1      | from     | int                     | -     | local node ID of edge departure                |
| 2      | to       | int                     | -     | local node ID of edge arrival                  |
| 3      | comments | string, list of strings | -     | any comments that can be attached to the edges | -->

### `*_node_pos.csv`


| Column | Name | Type  | Units | Description                                |
| -------- | ------ | ------- | ------- | -------------------------------------------- |
| 1      | id   | int   | -     | local node ID                              |
| 2      | x    | float | m     | coordinates in the x direction (easting)   |
| 3      | y    | float | m     | coordinates in the y direction (northing)  |
| 4      | z    | float | m     | coordinates in the z direction (elevation) |

### `*_node_csdim.csv`


| Column | Name      | Type  | Units | Description            |
| -------- | ----------- | ------- | ------- | ------------------------ |
| 1      | from      | int   | -     | local node ID          |
| 2      | cs_width  | float | m     | cross-sectional width  |
| 3      | cs_height | float | m     | cross-sectional height |

<!-- ### `*_node_flags.csv`


| Column | Name     | Type                        | Units | Description                    |
| -------- | ---------- | ----------------------------- | ------- | -------------------------------- |
| 1      | id       | int                         | -     | local node ID                  |
| 3      | comments | string, list of stringsfloa | -     | any flags attached to the node | -->

<!-- ### `*_node_comments.csv`


| Column | Name     | Type                    | Units | Description                       |
| -------- | ---------- | ------------------------- | ------- | ----------------------------------- |
| 1      | from     | int                     | -     | local node ID                     |
| 3      | comments | string, list of strings | -     | any comments attached to the node | -->

<!-- ### `*_node_splays.csv`


| Column | Name | Type  | Units | Description                                                              |
| -------- | ------ | ------- | ------- | -------------------------------------------------------------------------- |
| 1      | id   | int   | -     | local node ID of the origin of the splay shot                            |
| 2      | x    | float | m     | coordinates in the x direction of the point of arrival of the splay shot |
| 3      | y    | float | m     | coordinates in the y direction of the point of arrival of the splay shot |
| 4      | z    | float | m     | coordinates in the z direction of the point of arrival of the splay shot |

### `*_node_idsql.csv`


| Column | Name  | Type | Units | Description   |
| -------- | ------- | ------ | ------- | --------------- |
| 1      | id    | int  | -     | local node ID |
| 2      | idsql | int  | -     | SQL node ID   |

### `*_node_fulladdress.csv`


| Column | Name        | Type   | Units | Description                                   |
| -------- | ------------- | -------- | ------- | ----------------------------------------------- |
| 1      | id          | int    | -     | local node ID                                 |
| 2      | fulladdress | string | -     | original data id and full address of the node | -->