using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmoGuyWPF.Model
{
	public class DataModel
	{
		SensorModel _AF3, _AF4, _F3, _F4, _P7, _FC6, _F7, _F8, _T7, _P8, _FC5, _T8, _O2, _O1;

		public SensorModel AF3 { get => _AF3; set => _AF3 = value; }
		public SensorModel AF4 { get => _AF4; set => _AF4 = value; }
		public SensorModel F3 { get => _F3; set => _F3 = value; }
		public SensorModel F4 { get => _F4; set => _F4 = value; }
		public SensorModel P7 { get => _P7; set => _P7 = value; }
		public SensorModel FC6 { get => _FC6; set => _FC6 = value; }
		public SensorModel F7 { get => _F7; set => _F7 = value; }
		public SensorModel F8 { get => _F8; set => _F8 = value; }
		public SensorModel T7 { get => _T7; set => _T7 = value; }
		public SensorModel P8 { get => _P8; set => _P8 = value; }
		public SensorModel FC5 { get => _FC5; set => _FC5 = value; }
		public SensorModel T8 { get => _T8; set => _T8 = value; }
		public SensorModel O2 { get => _O2; set => _O2 = value; }
		public SensorModel O1 { get => _O1; set => _O1 = value; }
	}
}
