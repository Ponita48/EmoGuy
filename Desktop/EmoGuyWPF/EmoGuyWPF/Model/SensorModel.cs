using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmoGuyWPF.Model
{
	public struct SensorModel
	{
		double _quality, _value;

		public double quality { get => _quality; set => _quality = value; }
		public double value { get => _value; set => _value = value; }
	}
}
