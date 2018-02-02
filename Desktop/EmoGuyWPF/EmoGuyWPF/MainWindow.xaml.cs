using EmoGuyWPF.Model;
using System;
using System.Collections.Generic;
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
		double counter;
		string old_data = "";
		public MainWindow()
		{
			InitializeComponent();
		}

		private void Button_Click(object sender, RoutedEventArgs e)
		{
			if (ws == null ||!ws.IsAlive)
			{
				connectToPython();

			}
		}
		public void OnMessageResult(object sender,MessageEventArgs e)
		{
			if (!old_data.Equals(e.Data))
			{
				old_data = e.Data;
				//displayData(e.Data);
				DataModel data = new DataModel();
				bool isParsed = false;
				try
				{
					data = new JavaScriptSerializer().Deserialize<DataModel>(e.Data);
					isParsed = true;
				}
				catch (Exception ex)
				{
					Console.WriteLine("error : " + ex.Message);
				}
				counter++;
				if (counter > 1000)
				{
				}
				if (isParsed)
				{
					this.Dispatcher.Invoke(() =>
					{

					});
				}

			}
		}
		public void connectToPython()
		{
			ws = new WebSocket("ws://"+txtIP.Text+":"+txtPort.Text+"/");
			ws.OnMessage += OnMessageResult;
			ws.Connect();
			isRunning = true;
			counter = 0;
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
