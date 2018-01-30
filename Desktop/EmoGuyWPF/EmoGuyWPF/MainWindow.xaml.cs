using EmoGuyWPF.Model;
using InteractiveDataDisplay.WPF;
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
		int counter;
		List<double> listDataAF3 = new List<double>();
		List<double> listDataAF4 = new List<double>();
		List<double> listDataF3 = new List<double>();
		List<double> listDataF4 = new List<double>();
		List<double> listDataF7 = new List<double>();
		List<double> listDataF8 = new List<double>();
		List<double> listDataFC5 = new List<double>();
		List<double> listDataFC6 = new List<double>();
		List<double> listDataT7 = new List<double>();
		List<double> listDataT8 = new List<double>();
		List<double> listDataP7 = new List<double>();
		List<double> listDataP8 = new List<double>();
		List<double> listDataO1 = new List<double>();
		List<double> listDataO2 = new List<double>();
		List<double> iteration = new List<double>();
		List<double> zeros = new List<double>();
		LineGraph LineAF3 = null;
		LineGraph LineAF4 = null;
		LineGraph LineF3 = null;
		LineGraph LineF4 = null;
		LineGraph LineF7 = null;
		LineGraph LineF8 = null;
		LineGraph LineFC5 = null;
		LineGraph LineFC6 = null;
		LineGraph LineT7 = null;
		LineGraph LineT8 = null;
		LineGraph LineP7 = null;
		LineGraph LineP8 = null;
		LineGraph LineO1 = null;
		LineGraph LineO2 = null;
		LineGraph LineZeros = null;
		public MainWindow()
		{
			InitializeComponent();
			LineAF3 = new LineGraph();
			LineAF4 = new LineGraph();
			LineF3 = new LineGraph();
			LineF4 = new LineGraph();
			LineF7 = new LineGraph();
			LineF8 = new LineGraph();
			LineFC5 = new LineGraph();
			LineFC6 = new LineGraph();
			LineT7 = new LineGraph();
			LineT8 = new LineGraph();
			LineP7 = new LineGraph();
			LineP8 = new LineGraph();
			LineO1 = new LineGraph();
			LineO2 = new LineGraph();
			LineZeros = new LineGraph();
			LineAF3.Stroke = new SolidColorBrush(Color.FromArgb(255, 95, 187, 110)) ;
			LineAF4.Stroke = new SolidColorBrush(Color.FromArgb(255, 23, 186, 155));
			LineF3.Stroke = new SolidColorBrush(Color.FromArgb(255, 83, 171, 209)) ;
			LineF4.Stroke = new SolidColorBrush(Color.FromArgb(255, 45, 129, 199)) ;
			LineF7.Stroke = new SolidColorBrush(Color.FromArgb(255, 146, 101, 182)) ;
			LineF8.Stroke = new SolidColorBrush(Color.FromArgb(255, 64, 167, 96)) ;
			LineFC5.Stroke = new SolidColorBrush(Color.FromArgb(255, 0, 167, 132)) ;
			LineFC6.Stroke = new SolidColorBrush(Color.FromArgb(255, 62, 141, 184)) ;
			LineT7.Stroke = new SolidColorBrush(Color.FromArgb(255, 85, 58, 129)) ;
			LineT8.Stroke = new SolidColorBrush(Color.FromArgb(255, 247, 217, 103)) ;
			LineP7.Stroke = new SolidColorBrush(Color.FromArgb(255, 250, 159, 42)) ;
			LineP8.Stroke = new SolidColorBrush(Color.FromArgb(255, 235, 106, 85)) ;
			LineO1.Stroke = new SolidColorBrush(Color.FromArgb(255, 162, 142, 131)) ;
			LineO2.Stroke = new SolidColorBrush(Color.FromArgb(255, 208, 71, 65)) ;
			LineZeros.Stroke = new SolidColorBrush(Colors.Black) ;
			linesContainer.Children.Add(LineAF3);
			linesContainer.Children.Add(LineAF4);
			linesContainer.Children.Add(LineF3);
			linesContainer.Children.Add(LineF4);
			linesContainer.Children.Add(LineF7);
			linesContainer.Children.Add(LineF8);
			linesContainer.Children.Add(LineFC5);
			linesContainer.Children.Add(LineFC6);
			linesContainer.Children.Add(LineT7);
			linesContainer.Children.Add(LineT8);
			linesContainer.Children.Add(LineP7);
			linesContainer.Children.Add(LineP8);
			linesContainer.Children.Add(LineO1);
			linesContainer.Children.Add(LineO2);
			linesContainer.Children.Add(LineZeros);
		}

		private void Button_Click(object sender, RoutedEventArgs e)
		{
			if (isOK)
			{
				ws.Close();
			}
			else
			{
				connectToPython();
			}

		}
		public void OnMessageResult(object sender,MessageEventArgs e)
		{
			this.Dispatcher.Invoke(() =>
			{
				try
				{
					DataModel data = new JavaScriptSerializer().Deserialize<DataModel>(e.Data);
					counter++;
					lblCounter.Content = "" + counter;
					if (counter > 300)
					{
						iteration.RemoveAt(0);
						listDataAF3.RemoveAt(0);
						listDataAF4.RemoveAt(0);
						listDataF3.RemoveAt(0);
						listDataF4.RemoveAt(0);
						listDataF7.RemoveAt(0);
						listDataF8.RemoveAt(0);
						listDataFC5.RemoveAt(0);
						listDataFC6.RemoveAt(0);
						listDataT7.RemoveAt(0);
						listDataT8.RemoveAt(0);
						listDataP7.RemoveAt(0);
						listDataP8.RemoveAt(0);
						listDataO1.RemoveAt(0);
						listDataO2.RemoveAt(0);
						zeros.RemoveAt(0);
					}
					iteration.Add(counter);
					listDataAF3.Add(data.AF3.value+7000);
					listDataAF4.Add(data.AF4.value + 6000);
					listDataF3.Add(data.F3.value + 5000);
					listDataF4.Add(data.F4.value + 4000);
					listDataF7.Add(data.F7.value + 3000);
					listDataF8.Add(data.F8.value + 2000);
					listDataFC5.Add(data.FC5.value + 1000);
					listDataFC6.Add(data.FC6.value);
					listDataT7.Add(data.T7.value - 1000);
					listDataT8.Add(data.T8.value - 2000);
					listDataP7.Add(data.P7.value - 3000);
					listDataP8.Add(data.P8.value - 4000);
					listDataO1.Add(data.O1.value - 5000);
					listDataO2.Add(data.O2.value - 6000);
					zeros.Add(0 - 6000);
					LineAF3.Plot(iteration, listDataAF3);
					LineAF4.Plot(iteration, listDataAF4);
					LineF3.Plot(iteration, listDataF3);
					LineF4.Plot(iteration, listDataF4);
					LineF7.Plot(iteration, listDataF7);
					LineF8.Plot(iteration, listDataF8);
					LineFC5.Plot(iteration, listDataFC5);
					LineFC6.Plot(iteration, listDataFC6);
					LineT7.Plot(iteration, listDataT7);
					LineT8.Plot(iteration, listDataT8);
					LineP7.Plot(iteration, listDataP7);
					LineP8.Plot(iteration, listDataP8);
					LineO1.Plot(iteration, listDataO1);
					LineO2.Plot(iteration, listDataO2);
					LineZeros.Plot(iteration, zeros);
				}
				catch (Exception ex)
				{
					Console.WriteLine("error : " + ex.Message);
				}
			});
		}
		public void connectToPython()
		{
			ws = new WebSocket("ws://"+txtIP.Text+":"+txtPort.Text+"/");
			ws.OnMessage += OnMessageResult;
			ws.Connect();
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
				iteration.Clear();
				listDataAF3.Clear();
				listDataAF4.Clear();
				listDataF3.Clear();
				listDataF4.Clear();
				listDataF7.Clear();
				listDataF8.Clear();
				listDataFC5.Clear();
				listDataFC6.Clear();
				listDataT7.Clear();
				listDataT8.Clear();
				listDataP7.Clear();
				listDataP8.Clear();
				listDataO1.Clear();
				listDataO2.Clear();
				zeros.Clear();
				ws.Send("STOP");
			}
			else
			{
				isRunning = true;
				counter = 0;
				ws.Send("START");
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
		//			string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
		//											CultureInfo.InvariantCulture);
		//			Console.WriteLine(timestamp);
		//			List<List<double>> listData = new List<List<double>>();
		//			List<string> header = new List<string>();
		//			using (var reader = new StreamReader(@"D:\magang\Project\result.csv"))
		//			{
		//				for (int i = 0; i < 14; i++)
		//				{
		//					listData.Add(new List<double>());
		//				}
		//				while (!reader.EndOfStream)
		//				{
		//					var line = reader.ReadLine();
		//					var values = line.Split(',');
		//					int x = 0;
		//					foreach (var item in values)
		//					{
		//						try
		//						{
		//							listData.ElementAt(x).Add(double.Parse(item));
		//						}
		//						catch (Exception ex)
		//						{
		//							header.Add(item);
		//							//Console.WriteLine(ex.Message);
		//						}
		//						x++;
		//					}
		//				}

		//			}
		//			string timestamp3 = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
		//											CultureInfo.InvariantCulture);
		//			Console.WriteLine(timestamp3);
		//			List<double> listY = new List<double>();
		//			for (double i = 0; i < listData.ElementAt(0).Count; i++)
		//			{
		//				listY.Add(i* 0.00390625);
		//			}
		////			Console.WriteLine("Panjang list y" + listY.Count);
		//	//		Console.WriteLine("Panjang list x" + listData.ElementAt(0).Count);
		//			int y = 0;
		//			foreach (var item in listData)
		//			{
		//				var lg = new LineGraph();
		//				linesContainer.Children.Add(lg);
		//				lg.Stroke = new SolidColorBrush(Color.FromArgb(255, 0, (byte)(y * 10), 0));
		//				lg.Description = "Data "+header.ElementAt(y);
		//				lg.StrokeThickness = 2;
		//				lg.Plot(listY, item);
		//				y++;

		//			}
		//			string timestamp2 = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff",
		//											CultureInfo.InvariantCulture);
		//			Console.WriteLine(timestamp2);
		//			//SeriesCollection seriesCollection = new SeriesCollection();
		//			//foreach (var item in listData)
		//			//{
		//			//	ChartValues<double> data = new ChartValues<double>();
		//			//	data.AddRange(item);
		//			//	seriesCollection.Add(new LineSeries
		//			//	{
		//			//		Values = data
		//			//	});

		//			//}
		//			//EEGChart.Series = seriesCollection;
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
