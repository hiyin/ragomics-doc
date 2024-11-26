# Platform Login and Registration

## Platform Login
On the login page, users can enter their account credentials (mobile number) and password, then click the **Log in** button to access the platform. If users do not have an account, they can click the **Register** button to proceed with account registration. In case users forget their password, they can click the **Forgot password** button to reset it.

## Account Registration
On the registration page, users need to input their username, password, and mobile number (used as the login account). After entering these details, users can click the **Send** button to receive and input a mobile verification code. If users do not have an invitation code, they can contact customer service by emailing **yuze@raganetwork.com** for assistance.

## Password Reset
On the password reset page, users must enter their mobile number (login account) and click the **Send** button to receive a mobile verification code. Users then input the verification code along with their new password. Once the information is filled in, they can click the **Next step** button to proceed to the password reset result page. If the reset is successful, users can click the **To login** button to return to the login page.

---

# Creation and Management of Analysis Tasks

## Workflow
After logging into the homepage, the **Workflow** tab includes two sections: **Analysis Task** and **Data Source**. 

- In the **Analysis Task** section, users can create and manage analysis tasks and view public analyses at the top of the page to explore examples of analyses provided by Ragomics.  
- In the **Data Source** section, users can import datasets from public databases into their accounts or upload data from local sources.

## Creating an Analysis
Once logged in, users can go to the **Analysis Task** page under the **Workflow** tab and click the **Create New Analysis Task** button to create a new analysis task. 

1. In the pop-up form, users must enter a name for the analysis task. While the task description is optional, it helps the **Agent** module provide more accurate assistance.  
2. Users can choose to enable the **With Guidance** feature. If enabled, the **Pipeline Helper** will automatically launch the first time the user accesses the analysis panel of the task, helping them quickly select an analysis pipeline tailored to their needs.  
3. Once the task is created, users will be directed to its **Analysis Panel**.

# Managing Analysis Tasks

## Viewing and Managing Analysis Tasks
After logging in, users can view and manage previously created analysis tasks in the **Workflow** - **Analysis Task** tab. Each analysis task card contains several buttons for task management:

- **Open Button**: Click to access the **Analysis Panel** of the selected task.
- **Collaborator Management Button**: Click to open the collaborator management page and invite collaborators to participate in the project analysis.
- **Edit Button**: Click to edit the task name and description.
- **Copy Button**: Click to duplicate the current analysis task. Note that the duplicated task will only retain the **Data Source** and any unexecuted analysis pipelines. Analysis results will not be copied.
- **Delete Button**: Click to delete the current analysis task. **This action is irreversible.**
- **Share Button**: Click to access the sharing page. Users can enable sharing for the task and click the quick copy link below to generate a shareable access URL. Other users can use the link to view the shared analysis task but cannot edit it as guest users.

---

## Collaborator Management
When an analysis task requires collaboration with other users, the **Collaborator List** can be opened. 

- Click the **Add Collaborator** button in the top-left corner to invite collaborators.
- Users can assign editing permissions to collaborators as needed.

# Public Analyses and Databases

## Public Analyses
Ragomics provides users with a series of completed analysis examples. Users can directly access these **Public Analyses** to review the analysis process and results. However, users cannot perform any editing actions on these public analyses.

---

## Public Databases
On the **Workflow** - **Data Source** page, users can explore datasets from public databases:

1. Click the **Show More** button to view additional datasets in the public database.
2. Select an interesting dataset and click the **Import** button to add it to the user's account database.

---

# Data Upload and Management

## Data Upload
Ragomics offers two methods for uploading data:

### Method 1
- Navigate to **Workflow** - **Data Source** - **My Data** section.
- Click the **Upload** button to start the data upload process.

### Method 2
- In the **Analysis Panel**, click the **Data Source** tab in the left sidebar.
- Click the **Upload from Device** button to begin uploading data directly from your device.


# Supported Data Formats for Upload in Ragomics

Ragomics currently supports the following five data formats for upload:

## 1. AnnData Upload
- Users can add `.h5ad` files by dragging and dropping or clicking the **Upload** button.  
- Select the corresponding species information and provide a description of the data.  
- Once the file is selected and all information is filled out, click the **Upload** button to start uploading.  
- When the upload status indicates success, the data upload is complete.

---

## 2. 10x Data Upload
1. Enter the data name, species information, and data description.  
2. Click the **Next Step** button, then click **Add a Sample** to create a new sample row.  
3. For multiple samples, add the corresponding number of sample rows.  
4. In each sample row, upload the following three files:  
   - `barcodes.tsv`  
   - `genes.tsv`  
   - `matrix.mtx`  
5. Once all data is uploaded, click the **Assemble** button to complete the upload process.

---

## 3. Assemble AnnData
1. Enter species information and data description, then click the **Next Step** button.  
2. Upload the required files by dragging and dropping or clicking the upload area:  
   - **Mandatory Files**:  
     - In the central **Layers** section, upload `X`, or `unspliced` and `spliced` files.  
     - `var`  
     - `obs`  
   - **Optional Files**:  
     - `obsp`  
     - `obsm`  
     - `varm`  
     - `varp`  
3. Once all files are uploaded, click the **Assemble** button to finalize the AnnData assembly.  
4. Click the **Complete** button to finish the upload process.

---

## 4. FastQ Upload
1. Select the corresponding species information and provide a description of the data.  
2. Click the **Next Step** button.  
3. Add FastQ `.zip` files by dragging and dropping or clicking the central upload area.

---

## 5. Spaceranger Count Upload
1. Enter the data name, select the corresponding species information, and provide a description of the data.  
2. Click the **Next Step** button.  
3. Add Spaceranger Count data by dragging and dropping or clicking the upload area.  
4. On the right side of the upload panel, you can find format requirements and mandatory file examples.  
5. Once the data is uploaded, click the **Assemble** button to complete the data assembly.

# Analysis Panel

In the **Analysis Panel**, users can freely perform various analysis operations, such as uploading data, importing data, selecting **Function Blocks**, and assembling analysis pipelines. After completing the analysis, users can view the results directly or navigate to the corresponding **Visualization Panel** to explore the visualized outcomes.

---

## Importing Data
In the **Analysis Panel**, users can import data through the **Data Source** tab on the left sidebar. There are three methods for importing data:

### 1. Importing from Existing Data
- If users have already uploaded the target data to their account via the data upload feature, they can choose to import it from existing data.  
- In the import form, select the desired data by checking the boxes on the left.  
- Click **Confirm** to import the data from the account into the current analysis task.

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

---

## Pipeline Template Library
In the **Pipeline Helper** page, users can select a suitable analysis pipeline from Ragomics' **Pipeline Template Library** and import it into the **Analysis Panel** for use.

---

## AI Pipeline
In the **Pipeline Helper** page, users can utilize the **AI Pipeline** feature:

1. Select the dataset to be analyzed and input the analysis requirements.  
   - If unsure about how to phrase the requirements, click **Request Templates** to view examples.  
2. After entering the analysis requirements, click **Next Step**.  
3. Ragomics will display the original requirements and the AI-optimized version.  
   - Users can compare the two, edit them if necessary, or refresh the AI-generated result if unsatisfied.  
4. Select the finalized requirement text and click **Confirm**.  
5. In the next step, choose to either query and match pipelines from the **Pipeline Template Library** or have the AI generate a new pipeline.  
6. Once the pipeline is generated, click **Import** to add it to the **Analysis Panel**.

---

## Analysis Nodes
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

### Node Design
- **Connection Zones**: Located on the left and right sides of the node for assembling pipelines.
- **Node Status**: Indicated by the color at the top of the node.
- **Node Name**: Displays the default name of the algorithm module. Users can click the edit button to customize the node name.

# Adjusting Parameters
Users can click the **Edit** button within an analysis node to open the parameter adjustment panel.

---

## Agent
The **Agent** functionality provides intelligent assistance for tasks within an analysis node.

---

## Visualization Panel
The **Visualization Panel** allows users to explore and interact with the visualized results of their analysis.


### Upload from data source
In the **Data source** management page, click ==Upload data from device== to upload data
![analysis-drag-into-panel](../../img/homepage-upload.png)

<div style="display: flex; align-items: center;">
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