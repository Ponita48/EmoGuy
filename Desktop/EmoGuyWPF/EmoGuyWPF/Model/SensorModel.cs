using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmoGuyWPF.Model
{
	public struct SensorModel
	{
		float _quality, _value;

		public float quality { get => _quality; set => _quality = value; }
		public float value { get => _value; set => _value = value; }
	}
}
