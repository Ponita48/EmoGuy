   M S B A M L   `   `   `  ����D  @EmoGuyWPF, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null%clr-namespace:EmoGuyWPF	EmoGuyWPF  5   	   l hSystem.Windows.Controls.DataVisualization.Toolkit, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null�{clr-namespace:System.Windows.Controls.DataVisualization.Charting;assembly=System.Windows.Controls.DataVisualization.Toolkit2System.Windows.Controls.DataVisualization.Charting 5          EmoGuyWPF.MainWindow   5   	   W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   U QMaterialDesignThemes.Wpf, Version=2.3.1.953, Culture=neutral, PublicKeyToken=nullFmaterialDesign1http://materialdesigninxaml.net/winfx/xaml/themes  5      :d2http://schemas.microsoft.com/expression/blend/2008  5      Dmc;http://schemas.openxmlformats.org/markup-compatibility/2006  5      #localclr-namespace:EmoGuyWPF  5   	   �charting{clr-namespace:System.Windows.Controls.DataVisualization.Charting;assembly=System.Windows.Controls.DataVisualization.Toolkit  5      -   5          � Title$  
MainWindow��5
   	   $	��768��63   $
��1280��6@   .��5      � .+�5      �� -   5        $��txtIP��5      )  #MaterialDesignThemes.Wpf.HintAssist   Hint$ e.g. : 127.0.0.1��6   $��Right=�6K   $��35��6g   $��	0,41,10,0q�6s    �� TextWrapping$
 Wrap=�6�   $��	127.0.0.1��6�   $	��Top=�6�   $	��203��6�   �� 5      -   5        $��txtPort��5      $ e.g. : 8080��6   $��Right=�6H   $��33��6d   $��
0,112,10,0q�6p   $
 Wrap=�6�   $
��8080��6�   $	��Top=�6�   $	��203��6�   �� 5      $��IP��6
   $��Right=�6   $��
0,10,155,0q�63   $	��Top=�6G   $��58��6_   �� 5      $
��PORT��6
   $��Right=�6   $��
0,81,174,0q�65   $	��Top=�6I   �� 5      -   5        $��Connect��5      $��Right=�6   $��0,204,125,0q�69   $	��Top=�6N   $��88��6f   6q   �� 5      $��Recoding Control��6   $��Right=�6'   $��0,278,10,98q�6C   $	��203��6X   .��5      �� $
��Auto=�6   .��5      � .+�5      �� $��F3��6   $	��Top=�6   �� 5      $	��FC5��6   $	��Top=�6   $��0,30,0,0q�67   �� 5      $��F7��6   $	��Top=�6   $��0,60,0,0q�66   �� 5      $��T7��6   $	��Top=�6   $��0,90,0,0q�66   �� 5      $��P7��6   $	��Top=�6   $��	0,120,0,0q�66   �� 5      $��O1��6   $	��Top=�6   $��	0,150,0,0q�66   �� 5      $��O2��6   $	��Top=�6   $��	0,180,0,0q�66   �� 5      $��P8��6   $	��Top=�6   $��	0,210,0,0q�66   �� 5      $��T8��6   $	��Top=�6   $��	0,240,0,0q�66   �� 5      $��F8��6   $	��Top=�6   $��	0,270,0,0q�66   �� 5      $	��AF4��6   $	��Top=�6   $��	0,300,0,0q�67   �� 5      $	��FC6��6   $	��Top=�6   $��	0,330,0,0q�67   �� 5       $��F4��6   $	��Top=�6   $��	0,360,0,0q�66   �� 5!      $	��AF3��6   $	��Top=�6   $��	0,390,0,0q�67   5#      5$      5%      �� 5&      $��Counter��6
   $��Right=�6   $��
0,0,125,10q�68   $��87��6L   $��83��6W   $��Bottom=�6c   $��20(�6~   �� 5'      -   5        $��
lblCounter��5'   
   $��0��6   $��Right=�6(   $��	0,0,10,10q�6D   $��Bottom=�6W   $��83��6r   $��94��6~   $��20(�6�   �� 5(      -   5        $��	SlideRate��5(      $��Right=�6   $��
0,181,10,0q�68   $	��Top=�6L   $	��202��6d    � Maximum$
 1000Q�6p    � Minimum$	 100Q�6    � LargeChange$ 10Q�6�    � SmallChange$ 1Q�6�    � Value$	 300Q�6�   �� 5)      -   5        $��
Disconnect��5)      $��Right=�6    $��
0,204,10,0q�6<   $	��Top=�6P   $	��110��6h   6t   �� 5*      $��Displayed Data Rate��6
   $��Right=�6(   $��
0,150,95,0q�6D   $	��Top=�6X   �� 5+      -   5        $��Reset��5+      $��Right=�6   $��
0,241,10,0q�67   $	��Top=�6K   $	��202��6c   6o   >  8System.Windows.Controls.DataVisualization.Charting.Chart  5�      $��Bottom=�6   $��
0,0,218,49q�6+      Series. 5�      C  =System.Windows.Controls.DataVisualization.Charting.LineSeries  H  BSystem.Windows.Controls.DataVisualization.Charting.DataPointSeries	   IsSelectionEnabled	 .  ?  9System.Windows.Controls.DataVisualization.Charting.Series
   Title$	
 AF3��5�   V      ItemsSource 6   ��  �� Path$ DataAF3�   IndependentValueBinding 5�      �� *Date+   DependentValueBinding 5�      �� *Value+  5�      	 .  $	
 AF4��5�   V    6   �� $ DataAF4� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 F3��5�   U    6   �� $ DataF3� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 F4��5�   U    6   �� $ DataF4� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 P7��5�   U    6   �� $ DataP7� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 P8��5�   U    6   �� $ DataP8� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $	
 FC5��5�   V    6   �� $ DataFC5� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $	
 FC6��5�   V    6   �� $ DataFC6� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 F7��5�   U    6   �� $ DataF7� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 F8��5�   U    6   �� $ DataF8� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 T7��5�   T    6   �� $ DatT7� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 T8��5�   U    6   �� $ DataT8� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 O1��5�   U    6   �� $ DataO1� 5�      �� *Date+ 5�      �� *Value+  5�      	 .  $
 O2��5�   U    6   �� $ DataO2� 5�      �� *Date+ 5�      �� *Value+5�      �� 5�      -	   5        $��textBoxTest��5�      $
��Left=�6   $��23��6:   $��1103,84,0,0q�6F   $
 Wrap=�6[   $��2��6o   $	��Top=�6x   $	��159��6�   5�      5�      