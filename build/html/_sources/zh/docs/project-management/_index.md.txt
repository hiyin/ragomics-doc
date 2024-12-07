# <span style="color:#00bfff">**Platform Login and Registration**</span>

## <span style="color:#00bfff">**Platform Login**</span>
On the login page, users can enter their account credentials (mobile number) and password, then click the **Log in** button to access the platform. If users do not have an account, they can click the **Register** button to proceed with <span style="color:#00bfff">account registration</span>. In case users forget their password, they can click the **Forgot password** button to <span style="color:#00bfff">reset password</span>.

## <span style="color:#00bfff">**Account Registration**</span>
On the registration page, users need to input their username, password, and mobile number (used as the login account). After entering these details, users can click the **Send** button to receive and input a mobile verification code. If users do not have an invitation code, they can contact customer service by emailing **yuze@raganetwork.com** for assistance.

## <span style="color:#00bfff">**Password Reset**</span>
On the password reset page, users must enter their mobile number (login account) and click the **Send** button to receive a mobile verification code. Users then input the verification code along with their new password. Once the information is filled in, they can click the **Next step** button to proceed to the password reset result page. If the reset is successful, users can click the **To login** button to return to the login page.

## <span style="color:#00bfff">**Guest Mode**</span>
If users do not have a platform account and prefer not to register, they can choose to log in as a guest (**Login as a guest**). In visitor mode, all editing operations will be disabled. However, guests can still view public analyses or those shared by other users.
![guest-mode](../../img/platform-login-and-registeration/image.png)

---

# <span style="color:#00bfff">**Creation and Management of Analysis Tasks**</span>

## <span style="color:#00bfff">**Workflow**</span>
After logging into the homepage, the <span style="color:#00bfff">Workflow</span> tab includes two sections: <span style="color:#00bfff">Analysis Task</span> and <span style="color:#00bfff">Data Source</span>. 

- In the <span style="color:#00bfff">Analysis Task</span> section, users can create and manage analysis tasks and view <span style="color:#00bfff">Public Analyses</span> at the top of the page to explore examples of analyses provided by Ragomics.  
- In the <<span style="color:#00bfff">Data Source</span> section, users can import datasets from <span style="color:#00bfff">Public Databases</span> into their accounts or <span style="color:#00bfff">Upload Data</span> from local sources.

## <span style="color:#00bfff">**Creating an Analysis**</span>
Once logged in, users can go to the <span style="color:#00bfff">Analysis Task</span> page under the <span style="color:#00bfff">Workflow</span> tab and click the **Create New Analysis Task** button to create a new analysis task. 

1. In the pop-up form, users must enter a name for the analysis task. While the task description is optional, it helps the <span style="color:#00bfff">**Agent**</span> module provide more accurate assistance.  
2. Users can choose to enable the **With Guidance** feature. If enabled, the <span style="color:#00bfff">Pipeline Helper</span> will automatically launch the first time the user accesses the <span style="color:#00bfff">Analysis Panel</span> of the task, helping them quickly select an analysis pipeline tailored to their needs.  
3. Once the task is created, users will be directed to its <span style="color:#00bfff">Analysis Panel</span>.
![create-analysis](../../img/analysis-creation-and-management/create-new-analysis-task.png)

## <span style="color:#00bfff">**Managing Analysis Tasks**</span>
After logging in, users can view and manage previously created analysis tasks in the <span style="color:#00bfff">Workflow</span> - <span style="color:#00bfff">Analysis Task</span> tab. Each analysis task card contains several buttons for task management. Click **Open** button on the analysis card to enter the **Analysis Panel** of the selected task.

- **Collaborator Management Button** (![collaborate-button](../../img/analysis-creation-and-management/collaborate-button.png)): Click to open the <span style="color:#00bfff">Collaborator Management</span> page and invite collaborators to participate in the project analysis.
- **Edit Button** (![edit-button](../../img/analysis-creation-and-management/edit-button.png)): Click to edit the task name and description.
- **Copy Button** (![copy-button](../../img/analysis-creation-and-management/copy-button.png)): Click to duplicate the current analysis task. Note that the duplicated task will only retain the **Data Source** and any unexecuted analysis pipelines. Analysis results will not be copied.
- **Delete Button** (![delete-button](../../img/analysis-creation-and-management/delete-button.png)): Click to delete the current analysis task. **This action is irreversible.**
- **Share Button** (![share-button](../../img/analysis-creation-and-management/share-button.png)): Click to access the sharing page. Users can enable sharing for the task and click the quick copy link below to generate a shareable access URL. Other users can use the link to view the shared analysis task but cannot edit it as guest users.

## <span style="color:#00bfff">**Collaborator Management**</span>
When an analysis task requires collaboration with other users, the **Collaborator List** can be opened. 

- Click the **Add Collaborator** (![add-collaborator-button](../../img/analysis-creation-and-management/add-collaborator-button.png)) button in the top-left corner to invite collaborators.
- Users can assign editing permissions to collaborators as needed.
- Once added, the invited collaborator must accept the invitation through the <span style="color:#00bfff">In-app Notifications</span> to access and edit the analysis task.

---

# <span style="color:#00bfff">**Public Analyses and Databases**</span>

## <span style="color:#00bfff">**Public Analyses**</span>
Ragomics provides users with a series of completed analysis examples. Users can directly access these **Public Analyses** to review the analysis process and results. However, users cannot perform any editing actions on these public analyses.

## <span style="color:#00bfff">**Public Databases**</span>
On the <span style="color:#00bfff">Workflow</span> - <span style="color:#00bfff">Data Source</span> page, users can explore datasets from public databases:

1. Click the **Show More** button to view additional datasets in the public database.
2. Select an interesting dataset and click the **Import** button to add it to the user's account database.

---

# <span style="color:#00bfff">**Data Upload and Management**</span>

## <span style="color:#00bfff">**Data Upload**</span>
Ragomics offers two methods for uploading data:

Method 1
- Navigate to <span style="color:#00bfff">Workflow</span> - <span style="color:#00bfff">Data Source</span> - **My Data** section.
- Click the **Upload** (![upload-button](../../img/data-upload-and-management/upload-button.png)) button to start the data upload process.

Method 2
- In the **Analysis Panel**, click the **Add** (![add-button](../../img/data-upload-and-management/add-button.png)) button under the Data Source tab on the left sidebar, choose **Upload from Device** button to begin uploading data directly from your device.
![upload-from-device](../../img/data-upload-and-management/upload-from-device.png)

Supported Data Formats for Upload in Ragomics

Ragomics currently supports the following five data formats for upload:

1. AnnData Upload
- Users can add `.h5ad` files by dragging and dropping or clicking the **Add** (![add-button](../../img/data-upload-and-management/anndata-add-button.png)) button.  
- Select the corresponding species information and provide a description of the data.  
- Once the file is selected and all information is filled out, click the **Upload** (![upload-button](../../img/data-upload-and-management/anndata-upload-button.png)) button to start uploading.  
- When the upload status indicates success ![complete-status](../../img/data-upload-and-management/complete-status.png), the data upload is complete.

2. 10x Data Upload
- Enter the data name, species information, and data description.  
- Click the **Next Step** button, then click **Add a Sample** to create a new sample row.  
- For multiple samples, add the corresponding number of sample rows.  
- In each sample row, upload the following three files:  
   - `barcodes.tsv`  
   - `genes.tsv`  
   - `matrix.mtx`  
- Once all data is uploaded, click the **Assemble** button to complete the upload process.

3. Assemble AnnData
- Enter species information and data description, then click the **Next Step** button.  
- Upload the required files by dragging and dropping or clicking the upload area:  
   - Mandatory Files:  
     - In the central **Layers** section, upload `X`, or `unspliced` and `spliced` files.  
     - `var`  
     - `obs`  
   - Optional Files:  
     - `obsp`  
     - `obsm`  
     - `varm`  
     - `varp`  
- Once all files are uploaded, click the **Assemble** button to finalize the AnnData assembly.  
- Click the **Complete** button to finish the upload process.

4. FastQ Upload
- Select the corresponding species information and provide a description of the data.  
- Click the **Next Step** button.  
- Add FastQ `.zip` files by dragging and dropping or clicking the central upload area.

5. Spaceranger Count Upload
- Enter the data name, select the corresponding species information, and provide a description of the data.  
- Click the **Next Step** button.  
- Add Spaceranger Count data by dragging and dropping or clicking the upload area.  
- On the right side of the upload panel, you can find format requirements and mandatory file examples.  
- Once the data is uploaded, click the **Assemble** button to complete the data assembly.
![spaceranger-count-upload](../../img/data-upload-and-management/spaceranger%20count%20upload.png)

## <span style="color:#00bfff">**Importing Data**</span>
In the **Analysis Panel**, users can import data through **Add** (![add-button](../../img/data-upload-and-management/add-button.png)) button under the <span style="color:#00bfff">Data Source</span> tab on the left sidebar. There are three methods for importing data:

### 1. Importing from Existing Data
- If users have already uploaded the target data to their account via the data upload feature, they can choose to import it from existing data.  
- In the import form, select the desired data by checking the boxes on the left.  
- Click **Confirm** to import the data from the account into the current analysis task.

---

# Analysis Panel

In the **Analysis Panel**, users can freely perform various analysis operations, such as uploading data, importing data, selecting **Function Blocks**, and assembling analysis pipelines. After completing the analysis, users can view the results directly or navigate to the corresponding **Visualization Panel** to explore the visualized outcomes.

## **<span style="color:#00bfff;">Automatic Layout</span>**  
Users can manually arrange the nodes of the analysis pipeline or enable an automatic layout feature. By clicking the button on the bottom toolbar of the analysis panel, users can activate automatic layout in the pop-up options. When enabled, any subsequently connected analysis nodes will be automatically arranged. To instantly rearrange the entire analysis pipeline, users can click the bottom toolbar button, and all nodes in the current analysis panel will be automatically laid out immediately.

## **<span style="color:#00bfff;">Analysis Pipeline Thumbnail</span>**
For large analysis pipelines that are difficult to overview, users can enable the thumbnail feature by clicking the button on the bottom toolbar of the analysis panel. The thumbnail allows users to quickly locate which part of the pipeline they are currently operating on within the broader analysis pipeline.

## **<span style="color:#00bfff;">Analysis Node Status Panel</span>** *(分析节点状态面板)*

If users need an overview of the status of all analysis nodes in the current pipeline, they can refer to the bottom toolbar. The toolbar displays the total number of nodes in the current panel, along with counts for nodes that are running, failed, successful, waiting, or under bug-fix debugging.  

Users can click the number next to "Nodes" to open the **Analysis Node Status Panel**. When the highlight setting is enabled, clicking any node card in the analysis panel will highlight the corresponding row in the status panel. Similarly, clicking a node name in the status panel will cause the analysis panel to focus on the corresponding node in the pipeline.  

Additionally, clicking the icons next to each node in the status panel allows users to view the code for that specific node.

## **<span style="color:#00bfff;">Sharing Analysis Tasks</span>**

To share a specific analysis task with others, users can click the **"Share"** button at the top of the analysis panel. In the pop-up window, enable the **"Public"** setting and click the **"Copy Link"** button to generate a link for the current analysis task. Other users can use this link to access and view the shared task; however, guest users will not be able to make edits.  

If editing permissions are required, users can manage collaborators in the settings below.

## **<span style="color:#00bfff;">In-App Notifications</span>**

When an analysis node runs successfully or fails, or when a user receives a collaboration invitation, the in-app notification button at the top of the analysis panel will display an alert. Clicking the button will show a list of all notifications, allowing users to view and respond to the information accordingly.

---

# Analysis Pipeline

## Assembling an Analysis Pipeline
1. In the **Analysis Panel**, select any dataset from either the **Public Data List** or the **Imported Data List** on the left sidebar.  
2. Drag the selected data into the main analysis area of the panel.  
3. Based on your analysis requirements, choose the appropriate algorithm modules and drag them into the main analysis area.  
4. Independent algorithm modules can be connected to uploaded single-cell sequencing data or other analysis nodes.  
5. To connect, select the connection point on one side and drag it to another function block or data node.

# Pipeline Helper and Analysis Nodes

## Pipeline Helper
If users require assistance when assembling analysis pipelines, they can enable **Guidance** during the creation of an analysis or click the **Pipeline Helper** button in the top-left corner of the main area in the **Analysis Panel**.

## Pipeline Template Library
In the **Pipeline Helper** page, users can select a suitable analysis pipeline from Ragomics' **Pipeline Template Library** and import it into the **Analysis Panel** for use.

Users can select analysis pipelines from Ragomics' **Pipeline Template Library** and import them into the analysis panel on the Analysis Pipeline Assistant page.  

If the template library does not have a suitable template, users can use the **AI Pipeline** feature to generate a new analysis pipeline.

---

# Analysis Nodes
In the **Analysis Panel**, each algorithm module connected within the analysis pipeline is referred to as an **Analysis Node**. Users can perform the following operations on nodes:

- **Activate Agent Functionality**: Start the intelligent agent for assistance.
- **Adjust Parameters**: Modify parameters as needed.
- **Run Analysis**: Execute the analysis for the node.
- **View Node Code**: Inspect the underlying code for the node.
- **Check Node Outputs**: Access the results generated by the node.
- **View Calculation Logs and Details**: Monitor the computation process.
- **Share Node**: Share the node with collaborators.
- **Configure Computational Resources**: Allocate resources for the node.
- **Download Node Data**: Export the data generated by the node.

Node Design
- **Connection Zones**: Located on the left and right sides of the node for assembling pipelines.
- **Node Status**: Indicated by the color at the top of the node.
- **Node Name**: Displays the default name of the algorithm module. Users can click the edit button to customize the node name.

# Adjusting Parameters
Users can click the **Edit** button within an analysis node to open the parameter adjustment panel.

# Running Analysis

When users need to run a specific analysis node, they have three options:

1. Users can click the "Update and Run" button in the parameter panel of the analysis node to run the current node.
2. Users can click the button on the node card of the analysis node to start the analysis.
3. Users can click the button on the node card of the analysis node, then select "Run Sub Tree" in the secondary popup. In this case, the node and all subsequent child nodes will be executed sequentially.

# Node States

In the analysis panel, there are four possible states for an analysis node:

1. <strong style="color:#00bfff;">Ready to Run</strong>: The top of the node card is white, indicating that the node has not been run yet.
2. <span style="color:#00bfff; font-weight:bold;">Running</span>: The top of the node card is gray, indicating that the node is currently running.
3. <span style="color:#00bfff; font-weight:bold;">Run Completed</span>: The top of the node card is green, indicating that the node has successfully run.
4. <span style="color:#00bfff; font-weight:bold;">Run Error</span>: The top of the node card is red, indicating that an error occurred during the node's run, requiring troubleshooting.

# <strong style="color: #00bfff; font-weight:bold;">Node Output Results</strong>

When certain nodes generate downloadable CSV files after execution, users can click the button on the analysis node card, select "Output" in the secondary popup, and choose the file they need to download.

# <strong style="color: #00bfff; font-weight:bold;">Calculation Logs</strong>

After a node has been calculated at least once, users can click the button on the analysis node card, select "Calculation Logs" in the secondary popup to view it. Users can click the export button to export the calculation logs as a CSV file and download it to their local machine.

# <strong style="color: #00bfff;">Calculation Details</strong>

After a node has been calculated at least once, users can click the button on the analysis node card, select "Calculation Details" in the secondary popup to view it.

# <strong style="color: #00bfff;">Share Node</strong>

When a user has opened a <span style="color: #00bfff;">Sharing analysis task</span> but wishes to focus on a specific analysis node to share with others, they can click the button on the analysis node card, select "Share" in the secondary popup. This action will automatically copy the link to the current node, and other users can access and view the shared analysis task using the link. 
Please note that guest users will not have permission to edit the shared analysis.

# <strong style="color: #00bfff;">Configure Computational Resources</strong>

When users analyze data or algorithm modules that require significant computational resources, they can click the button on the analysis node card, select "Configure Computational Resources" in the secondary popup, and choose parameters like CPU, memory, timeout limits, etc., according to their needs. After configuration, the node will follow this setup when running.

# <strong style="color: #00bfff;">Download Node Data</strong>

After a node completes its calculation, users can click the button on the top-right of the analysis node card to download the current node's h5ad file.

# <strong style="color: #00bfff;">Chart Display</strong>

After an analysis node with charting functionality completes its execution, users can click the button in the toolbar at the bottom of the analysis panel to enable "Show Chart." The chart output will be displayed at the bottom of the node, and clicking the chart will redirect to the corresponding <span style="color: #00bfff;">visualization panel</span> page.

# <strong style="color: #00bfff;">Stop Analysis</strong>

If users need to stop the current running analysis process for any reason, they can click the button on the analysis node card, and in the secondary popup, select "Cancel Calculation."

If multiple analysis nodes are running simultaneously and the user wants to stop all computations at once, they can click the "Stop All" button in the toolbar at the bottom of the analysis panel.


# <span style="color: #00bfff; font-size: 32px;"><strong>Agent</strong></span>

An agent is a series of AI-assisted analysis features based on large language models in Ragomics.

## <span style="color: #00bfff;"><strong>AI Pipeline</strong></span>

In the AI Pipeline Helper page, users can utilize the AI Pipeline feature to select the data they wish to analyze and input their analysis requirements. If the user is unsure about how to input the analysis requirements, they can click on the <span style="color: #00bfff;">Request Templates</span> on the page to obtain examples. After filling in the analysis requirements, the user clicks "Next." Ragomics will display the user’s original requirements alongside the AI-optimized version. Users can compare the two and click the button to edit. If the user is dissatisfied with the current AI-generated optimized result, they can click the button to refresh it. The user needs to select the final requirements text to use and click the "Confirm" button. In the next step, the user must choose between querying analysis pipelines from the <span style="color: #00bfff;">Pipeline Template</span> library or generating an analysis pipeline directly through AI. After generation, they can click the "Import" button to bring the current generated analysis pipeline into the analysis panel.

## <span style="color: #00bfff;"><strong>AI Parameter</strong></span>

If users encounter difficulties when filling in the parameters for an analysis node, they can click the AI Parameter button at the bottom-left of the parameter panel. In the popup menu, users can select either <span style="color: #00bfff;">Fill All Parameters</span> or <span style="color: #00bfff;">Complete Unfilled Parameters</span>.

- **Fill All Parameters**: In this case, the agent will automatically fill in the appropriate parameters based on the user’s current analysis data, pipeline, and analysis node.
  
- **Complete Unfilled Parameters**: In this case, the agent will retain the existing parameters and automatically complete the remaining parameters based on the user’s current analysis data, pipeline, and analysis node.

When users click the Show Parameter Update History button, a popup will display the entire history of parameters generated using the AI Parameter function in this node.

## <span style="color: #00bfff;"><strong>Error Fixing</strong></span>

During the analysis process, users may encounter errors in certain analysis nodes. In such cases, users can click on the erroring node, and the error message for that node will appear on the right side of the analysis panel. The error message includes a description of the error, suggested fixes, and logs. Users can use this information to manually fix the error.

If users are still unable to fix the error, they can try using the <span style="color: #00bfff;">Bug Fixer</span> to resolve the issue. Users can click the button in the toolbar at the bottom of the analysis panel, select the Bug Fixer option in the popup, and input the maximum retry count for fixing. Afterward, they can re-run the erroring node, and the <span style="color: #00bfff;">Bug Fixer</span> will automatically attempt to fix the error.

## <span style="color: #00bfff;"><strong>AI Interpretation</strong></span>

Once an analysis node has completed execution, users can click to select the node. In the <span style="color: #00bfff;">AI Interpretation</span> section of the control panel on the right, users can click "Generate," and the agent module will provide biological interpretations of the data from that node, along with suggestions for subsequent analysis.

# <span style="color:#00bfff">**Visualization Panel**</span>  
Once the user completes the run of any analysis node, they can click the analysis node and open the **Visualization Panel** by clicking the top of the right panel. The **Visualization Panel** is divided into three sections: **Data Information Area**, **Main Image Display and Plotting Function Area**, and **Cell and Gene Group Management Area**.

## <span style="color:#00bfff">**Data Information Area**</span>  
The **Data Information Area** includes the **Observations (obs)** tab, **Gene List** tab, and **Observations Matrix (obsm)** tab.

- <span style="color:#00bfff">**Observations (obs) Tab**</span>  
  The **Observations Tab** contains two data blocks: **Cell Categories (category)** and **Continuous Values (Continuous)**.

  - <span style="color:#00bfff">**Cell Categories (category) Data Area**</span>  
    In the **Cell Categories (category) Data Area**, metadata about cells is displayed, such as cell types and sample information. This helps users better understand the data characteristics and background information of each cell.  

  - <span style="color:#00bfff">**Cell Categories (category) Coloring**</span>  
    When the main image display is in Embedding mode, users can click the button next to any dimension of the cell category to color the plot based on that category.
    
    Users can expand the cell category row to view subcategories under the current cell category and define the colors for these subcategories manually by clicking the color block icon next to each one.

  - <span style="color:#00bfff">**Subcategory Clustering Analysis**</span>  
    If users want to perform clustering on subcategories of a specific cell category, they can click the button next to that subcategory and choose the clustering algorithm to apply. After the algorithm completes, they can view the results in the corresponding analysis node.

  - <span style="color:#00bfff">**Cell Category Display Control**</span>  
    Users can toggle the display of cell categories or subcategories by clicking the buttons next to them, which helps users focus on specific cells within the Embedding page.

  - <span style="color:#00bfff">**Continuous Values (Continuous)**</span>  
    In the **Continuous Values** data area, users can select one or more continuous values to color the plot. They can also choose a color scheme for the coloring or manually define the colors for the start, middle, and end of the continuous values.

    If users want to filter cells based on continuous values, they can click the button next to the continuous value to expand the histogram and filter cells accordingly.

    Users can also set the **X-axis** or **Y-axis** of the Embedding plot directly using buttons next to the continuous values or genes.

- <span style="color:#00bfff">**Observations (obs) Tab Data Changes**</span>  
  As analysis progresses, changes in cell categories and continuous values will appear in the **Observations Tab**. Users can click the **Filter** button at the top to filter the displayed data based on the following conditions:
  - **All**: Includes all cell categories and continuous values from the current analysis node.
  - **New**: Only shows the newly generated data from the current analysis node.
  - **Changed**: Shows data that has been modified in the current node.
  - **Unchanged**: Displays data that has not been modified in the current node, usually inherited from previous analysis nodes.
  - **Deleted**: Displays only the deleted data, which cannot be modified.
  - **Annotation Generated**: Displays only cells with generated cell annotations (Cell Type Annotation).

- <span style="color:#00bfff">**Gene List (gene)**</span>  
  In the **Gene List Tab**, users can select one or more genes to color the plot. They can also choose a color scheme for the genes or manually define the colors for their start, middle, and end values.

  Users can also set a gene to the **X-axis** or **Y-axis** directly by clicking buttons next to the gene row.

## <span style="color:#00bfff">**Main Image and Plotting Function Area**</span>  
The **Main Image and Plotting Function Area** contains tabs for different image options. Users can click on a tab to view the images generated by various algorithm modules. Common image tabs like **Embedding**, **Pathway**, and **Plot** are always present in each analysis node. An image tab with a red dot indicates that it was newly generated in the current analysis node.

### **Quick Gene Algorithms**  
  The **Main Image and Plotting Function Area** contains quick access to algorithms such as **Highly Variable Genes (HVG)** and **Rank Genes Group**.
  
  - Users can click the **HVG** button to input the number of highly variable genes and run the algorithm. The result can be viewed after the algorithm completes.
  
  - Users can click the **Rank Genes Group** button to select subcategories under the **Cell Categories** tab. After selecting the subcategories, they can choose the method for ranking genes and run the algorithm. The results will be available in the corresponding analysis node after completion.

### <span style="color:#00bfff">**Embedding**</span>  
- **Dimension Selection**  
  In the **Embedding** image tab, users can click the **2D/3D Toggle** button to switch between 2D and 3D views. Clicking the **Dimensions** button will display a list of dimensions generated by the current and previous analysis nodes. Users can quickly switch between them. If custom dimensions are needed, users can choose the **Select Dimensions** option to set **X-axis**, **Y-axis**, and **Z-axis** in a popup.

- **Cell Selection**  
  Users can click the **Drag** button at the top of the **Embedding** image tab to enter selection mode. They can then click on the starting point and drag to form a selection box around the desired cells. Once the selection is closed, only the selected cells will be displayed. Users can save the selected cells as a **Cell Set** for further analysis.

- **Cell Filtering**  
  In **Continuous Values** and **Gene Coloring**, users can filter cells directly in the **Embedding** image tab using histograms. Users can also filter cells by adjusting sliders to refine the displayed cells.

- **Color Clipping**  
  The **Clipping** feature in the **Embedding** page helps manage color gradients in plots. The user can adjust the sliding bars to control where the color transition should start and end.

- **Resetting Filters and Operations**  
  After performing various filtering operations, users can click the **Filter** button in the **Embedding** page to reset the filters. Clicking the **Reset** button restores the visualization to its initial state.

- **Full Screen**  
  Users can toggle full-screen mode by clicking the full-screen button at the top of the **Embedding** page. Clicking it again exits full-screen mode.

- **Graph Download**  
  Users can download the current visualization by clicking the **Download** button and selecting the desired image format.

- **Plot Beautification Settings**  
  **Embedding** provides several customization options to beautify the plots, including:
  - **Coordinate Axes**: Users can toggle the visibility of axes or adjust their appearance.
  - **Cell Labels**: Users can toggle the display of cell labels on scatter plots and adjust their appearance.
  - **Cell Category Legend**: Users can toggle the display of the cell category legend and adjust its appearance.

### <span style="color:#00bfff">**Pathway**</span>  
In the **Pathway Tab**, users can create, view, and manage Pathway calculation results.

- **Create Pathway**  
  Users can click the button in the **Pathway Tab**, input a task name, select the gene set and species, choose the required library, and click **OK** to start the pathway analysis. After completion, the results will be available in the corresponding analysis node.

- **View Pathway**  
  The **Pathway Tab** lists the current and previous Pathway tasks. Users can click any task to view details and return to the task list.

### <span style="color:#00bfff">**Plot**</span>  
In the **Plot Tab**, users can toggle between different plot types, such as bar plots and violin plots.

- **Bar Plot**  
  In the **Bar Plot** mode, users can click a **Cell Category** and select an **X-axis** to create the bar plot.

- **Violin Plot**  
  In **Violin Plot** mode, users can choose an **X-axis** and either **obs** continuous values or a **Gene Set** for the **Y-axis** to generate a violin plot.

##  **<span style="color:#00bfff">Cell and Gene Group Management Area</span> ##

### **<span style="color:#00bfff">Cell Sets</span>**
Apart from saving cell sets on the Embedding page, users can also create cell sets by clicking the button under the **<span style="color:#00bfff">Cell Sets</span>** tab. Additionally, users can upload an existing cell set CSV file by clicking the button under the **<span style="color:#00bfff">Cell Sets</span>** tab to create a cell set.

Once the cell set is created, users can click the button next to the cell set to save the current cell set to the **<span style="color:#00bfff">Cell Type Annotation</span>** group (cell type annotation). Users can also click the button next to the cell set and choose the required clustering algorithm or use the cell set as target data for analysis.

### **<span style="color:#00bfff">Gene Sets</span>**
Users can create gene sets by clicking the button under the **<span style="color:#00bfff">Gene Sets</span>** tab. Users can also upload an existing gene set CSV file by clicking the button under the **<span style="color:#00bfff">Gene Sets</span>** tab to create a gene set. Once the gene set is created, users can click the button to export the gene set as a CSV file.

Users can click any gene set or the button next to the gene in the gene set to select a single-color or multi-color mode and use the gene set or gene for coloring the plot. When a gene set or gene is colored, users can click the button to choose a different color scheme for the current coloring. Users can also click the color block icon next to each gene set or gene to manually define the color used for each gene in the gene set.

When in the **<span style="color:#00bfff">Cell Type Annotation</span>** state (cell type annotation) process, if users don't want to display gene expression only for unannotated cells, they can click the **hide anno** button next to the gene set, which will exclude the already annotated cells and re-calculate and draw the histogram of the expression levels.

### **<span style="color:#00bfff">Cell Type Annotation</span>**
When users need to annotate cell types, they can click the **<span style="color:#00bfff">Cell Type Annotation</span>** tab and select either **manual annotation** or **automatic annotation** by clicking the button.

#### **<span style="color:#00bfff">Manual Annotation</span>**
After creating the annotation group, users can click the button, and the cell category area will enter the selection state. Users can select options in the checkboxes on the right of the cell subcategories. After selection, they can click to save the selected subcategory cells to the cell annotation group. **Overwrite**

Once all the cells are annotated, users can click the button to save the annotation results to **obs** (observations).

#### **<span style="color:#00bfff">Automatic Annotation</span>**
After selecting **automatic annotation**, users choose the model type that matches the source data species type and the corresponding annotation category. After clicking OK, the analysis panel will appear, and the automatic annotation analysis node will run. Once completed, users can view the analysis results in the visualization panel of the analysis node.

<div style="display: none; align-items: center;">
  <div style="flex: 1; padding-right: 10px;">
    <p>
      This is a paragraph on the left. You can provide details about the content
      here, explain the context, or introduce the video that appears on the right.
    </p>
  </div>
  <div style="flex: 1; padding-left: 10px;">
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
  </div>
</div>