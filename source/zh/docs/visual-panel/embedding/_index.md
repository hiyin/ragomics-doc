

# 细胞散点图Scatter/Embedding交互

散点图（Scatter）内，**每个散点代表一个细胞**。


## 切换基（Basis）
如basis中无选项，请通过平台计算相关basis或上传带有basis的数据，例如PCA、UMAP。计算完成后打开计算节点对应可视化界面Visual Panel。PCA、UMAP、t-SNE等降维结果显示在basis下拉菜单内。

下图basis选取为umap。如需切换basis可视化，点击Visual panel embedding区内basis下拉菜单进行选择  
{{< image src="images/visual-panel-endocrinogenesis-embedding-umap.png" alt="Alt text for the image" width="500px">}}

切换为PCA  
{{< image src="images/visual-panel-endocrinogenesis-embedding-pca.png" alt="Alt text for the image" width="500px">}}

下拉菜单中选择select dimensions可组合不同basis  
{{< image src="images/visual-panel-endocrinogenesis-embedding-basis-switch.png" alt="Alt text for the image" width="500px">}}

## 自定义x/y/z坐标（Customize x, y, z axes）


- 通过basis选取
- 通过基因的值选取
- 通过obs细胞的值选取

### 基（Basis combinattion）
Ragomics支持混合不同basis用于可视化。例如PCA产出的principle components（PCs）代表不同含义，您可通过选择PC及通过染色理解PC。
{{< image src="images/visual-panel-endocrinogenesis-embedding-basis-combination.png" alt="Alt text for the image" width="500px">}}

## 染色


### 通过obs-category进行染色
通过点击左侧obs区具体subcategory隐藏某一分类。常用的场景包括隐藏个别sample、cluster，方便数据可视化。  


### 通过obs-numerical进行染色
{{< image src="images/visual-panel-obs-embedding-numerical.png" alt="Alt text for the image" width="500px">}}

### 基因（Gene values）


## 细调图像
{{< image src="images/visual-panel-embedding-plot-0.png" alt="Alt text for the image" width="500px">}}



## 常用降维方法
- PCA：一般preprocess recipe内自动计算PCA
   - PCs数量一般根据explained variance elbow plot选取（实际中不少论文使用包默认PCs参数）
   - Scanpy, Seurat等代码库可手动计算pca（如已跑recipe，不需再进行PCA计算）
- UMAP：
   - Python: 
      - sc.tl.umap；dyn.reduceDimension等功能块可计算UMAP
      - 一般底层算法均基于umap-learn：https://umap-learn.readthedocs.io/en/latest/
   - R:
      - Seurat.RunUMAP
   - "Math salad" - from Dr. Lior Patcher, on X (former twitter)
- t-sne