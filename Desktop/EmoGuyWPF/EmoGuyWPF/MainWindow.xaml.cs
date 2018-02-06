using EmoGuyWPF.Model;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web.Script.Serialization;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using WebSocketSharp;

namespace EmoGuyWPF
{
	/// <summary>
	/// Interaction logic for MainWindow.xaml
	/// </summary>
	/// 

	public partial class MainWindow : Window
	{
		bool isOK = false;
		bool isRunning = false;
		WebSocket ws;
		float counter;
		string old_data = "";
		public MainWindow()
		{
			InitializeComponent();
			DataContext = this;
		}

		private void Button_Click(object sender, RoutedEventArgs e)
		{
			if (ws == null || !ws.IsAlive)
			{
				connectToPython();

			}
		}
		public void OnMessageResult(object sender, MessageEventArgs e)
		{
			counter++;
			if (!old_data.Equals(e.Data))
			{
				old_data = e.Data;
				//displayData(e.Data);
				DataModel data = new DataModel();
				bool isParsed = false;
				float mean = (float)4167.9950522878;
				try
				{
					data = new JavaScriptSerializer().Deserialize<DataModel>(e.Data);
					isParsed = true;
				}
				catch (Exception ex)
				{
					Console.WriteLine("error : " + ex.Message);
				}
				if (isParsed)
				{
					this.Dispatcher.Invoke(() =>
					{
						lblCounter.Content = counter;
					});
					this.Dispatcher.Invoke(() =>
					{
						if (counter > SlideRate.Value)
						{
							DataAF3.RemoveAt(0);
							DataAF4.RemoveAt(0);
							DataF3.RemoveAt(0);
							DataF4.RemoveAt(0);
							DataP7.RemoveAt(0);
							DataP8.RemoveAt(0);
							DataFC5.RemoveAt(0);
							DataFC6.RemoveAt(0);
							DataF7.RemoveAt(0);
							DataF8.RemoveAt(0);
							DataT7.RemoveAt(0);
							DataT8.RemoveAt(0);
							DataO1.RemoveAt(0);
							DataO2.RemoveAt(0);
						}
						DataAF3.Add(new Point(counter, data.AF3.value-mean));
						DataAF4.Add(new Point(counter, data.AF4.value - mean));
						DataF3.Add(new Point(counter, data.F3.value - mean));
						DataF4.Add(new Point(counter, data.F4.value - mean));
						DataP7.Add(new Point(counter, data.P7.value - mean));
						DataP8.Add(new Point(counter, data.P8.value - mean));
						DataFC5.Add(new Point(counter, data.FC5.value - mean));
						DataFC6.Add(new Point(counter, data.FC6.value - mean));
						DataF7.Add(new Point(counter, data.F7.value - mean));
						DataF8.Add(new Point(counter, data.F8.value - mean));
						DataT7.Add(new Point(counter, data.T7.value - mean));
						DataT8.Add(new Point(counter, data.T8.value - mean));
						DataO1.Add(new Point(counter, data.O1.value - mean));
						DataO2.Add(new Point(counter, data.O2.value - mean));
					});
				}

			}
		}
		public void connectToPython()
		{
			ws = new WebSocket("ws://" + txtIP.Text + ":" + txtPort.Text + "/");
			ws.OnMessage += OnMessageResult;
			ws.Connect();
			isRunning = true;
			counter = 0;
			DataAF3.Clear();
			DataAF4.Clear();
			DataF3.Clear();
			DataF4.Clear();
			DataP7.Clear();
			DataP8.Clear();
			DataFC5.Clear();
			DataFC6.Clear();
			DataF7.Clear();
			DataF8.Clear();
			DataT7.Clear();
			DataT8.Clear();
			DataO1.Clear();
			DataO2.Clear();
			ws.Send("START");

			counter = 0;
		}
		private void StartButton_Click(object sender, RoutedEventArgs e)
		{
			if (isRunning)
			{
				isRunning = false;
				//linesContainer.Children.Remove(LineAF3);
				//linesContainer.Children.Remove(LineAF4);
				//linesContainer.Children.Remove(LineF3);
				//linesContainer.Children.Remove(LineF4);
				//linesContainer.Children.Remove(LineF7);
				//linesContainer.Children.Remove(LineF8);
				//linesContainer.Children.Remove(LineFC5);
				//linesContainer.Children.Remove(LineFC6);
				//linesContainer.Children.Remove(LineT7);
				//linesContainer.Children.Remove(LineT8);
				//linesContainer.Children.Remove(LineP7);
				//linesContainer.Children.Remove(LineP8);
				//linesContainer.Children.Remove(LineO1);
				//linesContainer.Children.Remove(LineO2);

				ws.Send("STOP");
			}
			else
			{
			}
		}

		private void Window_Closed(object sender, EventArgs e)
		{
			try
			{
				ws.Close();
			}
			catch (Exception)
			{

			}
		}

		private void Button_Click_1(object sender, RoutedEventArgs e)
		{
			try
			{

				ws.Close();
			}
			catch (Exception)
			{

			}
		}

		private void Button_Click_2(object sender, RoutedEventArgs e)
		{
			counter = 0;
			DataAF3.Clear();
			DataAF4.Clear();
			DataF3.Clear();
			DataF4.Clear();
			DataP7.Clear();
			DataP8.Clear();
			DataFC5.Clear();
			DataFC6.Clear();
			DataF7.Clear();
			DataF8.Clear();
			DataT7.Clear();
			DataT8.Clear();
			DataO1.Clear();
			DataO2.Clear();
		}
		ObservableCollection<Point> _dataAF3 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataAF4 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataF4 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataF3 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataP7 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataP8 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataFC5 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataFC6 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataF7 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataF8 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataT7 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataT8 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataO1 = new ObservableCollection<Point>();
		ObservableCollection<Point> _dataO2 = new ObservableCollection<Point>();
		public ObservableCollection<Point> DataAF3
		{
			get { return _dataAF3; }
		}
		public ObservableCollection<Point> DataAF4
		{
			get { return _dataAF4; }
		}
		public ObservableCollection<Point> DataF3
		{
			get { return _dataF3; }
		}
		public ObservableCollection<Point> DataF4
		{
			get { return _dataF4; }
		}
		public ObservableCollection<Point> DataP7
		{
			get { return _dataP7; }
		}
		public ObservableCollection<Point> DataP8
		{
			get { return _dataP8; }
		}
		public ObservableCollection<Point> DataFC5
		{
			get { return _dataFC5; }
		}
		public ObservableCollection<Point> DataFC6
		{
			get { return _dataFC6; }
		}
		public ObservableCollection<Point> DataF7
		{
			get { return _dataF7; }
		}
		public ObservableCollection<Point> DataF8
		{
			get { return _dataF8; }
		}
		public ObservableCollection<Point> DataT7
		{
			get { return _dataT7; }
		}
		public ObservableCollection<Point> DataT8
		{
			get { return _dataT8; }
		}
		public ObservableCollection<Point> DataO1
		{
			get { return _dataO1; }
		}
		public ObservableCollection<Point> DataO2
		{
			get { return _dataO2; }
		}
		public class Point : DependencyObject
		{
			public static readonly DependencyProperty _date = DependencyProperty.Register("Date", typeof(float), typeof(Point));
			public Point(float date, float value)
			{
				Date = date;
				Value = value;
			}
			public float Date
			{
				get { return (float)GetValue(_date); }
				set { SetValue(_date, value); }
			}
			public static readonly DependencyProperty _value = DependencyProperty.Register("Value", typeof(float), typeof(Point));
			public float Value
			{
				get { return (float)GetValue(_value); }
				set { SetValue(_value, value); }
			}
			//private void Button_Click_3(object sender, RoutedEventArgs e)
			//{
			//	string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
			//									CultureInfo.InvariantCulture);
			//	Console.WriteLine(timestamp);
			//	List<List<double>> listData = new List<List<double>>();
			//	List<string> header = new List<string>();
			//	using (var reader = new StreamReader(@"D:\magang\Project\result.csv"))
			//	{
			//		for (int i = 0; i < 14; i++)
			//		{
			//			listData.Add(new List<double>());
			//		}
			//		while (!reader.EndOfStream)
			//		{
			//			var line = reader.ReadLine();
			//			var values = line.Split(',');
			//			int x = 0;
			//			foreach (var item in values)
			//			{
			//				try
			//				{
			//					listData.ElementAt(x).Add(double.Parse(item));
			//				}
			//				catch (Exception ex)
			//				{
			//					header.Add(item);
			//					//Console.WriteLine(ex.Message);
			//				}
			//				x++;
			//			}
			//		}

			//	}
			//	string timestamp3 = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
			//									CultureInfo.InvariantCulture);
			//	Console.WriteLine(timestamp3);
			//	List<double> listY = new List<double>();
			//	for (double i = 0; i < listData.ElementAt(0).Count; i++)
			//	{
			//		listY.Add(i * 0.00390625);
			//	}
			//	//			Console.WriteLine("Panjang list y" + listY.Count);
			//	//		Console.WriteLine("Panjang list x" + listData.ElementAt(0).Count);
			//	int y = 0;
			//	foreach (var item in listData)
			//	{
			//		var lg = new LineGraph();
			//		linesContainer.Children.Add(lg);
			//		lg.Stroke = new SolidColorBrush(Color.FromArgb(255, 0, (byte)(y * 10), 0));
			//		lg.Description = "Data " + header.ElementAt(y);
			//		lg.StrokeThickness = 2;
			//		lg.Plot(listY, item);
			//		y++;

			//	}
			//	string timestamp2 = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
			//									CultureInfo.InvariantCulture);
			//	Console.WriteLine(timestamp2);
			//	//SeriesCollection seriesCollection = new SeriesCollection();
			//	//foreach (var item in listData)
			//	//{
			//	//	ChartValues<double> data = new ChartValues<double>();
			//	//	data.AddRange(item);
			//	//	seriesCollection.Add(new LineSeries
			//	//	{
			//	//		Values = data
			//	//	});

			//	//}
			//	//EEGChart.Series = seriesCollection;
			//}
			//public void test()
			//{
			//	ws = new WebSocket("ws://127.0.0.1:8080");
			//	ws.OnMessage += OnMessageReceived;
			//	//ws.Connect();

			//}
			//public void OnMessageReceived(Object sender,MessageEventArgs e)
			//{

			//}

			//private void Button_Click(object sender, RoutedEventArgs e)
			//{
			//	ws.Send("Hallo");
			//}

			//private void Button_Click_1(object sender, RoutedEventArgs e)
			//{
			//	ws.ConnectAsync();
			//}
		}
	}
}
