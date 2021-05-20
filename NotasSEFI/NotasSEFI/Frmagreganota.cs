using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NotasSEFI
{
    public partial class Frmagreganota : Form
    {
        public Frmagreganota()
        {
            InitializeComponent();
        }

        private void txtpreciounitario_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar >= 32 && e.KeyChar <= 47) || (e.KeyChar >= 58 && e.KeyChar <= 255))
            {
                MessageBox.Show("Solo Números", "Alerta", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                e.Handled = true;
                return;
            }
        }

        private void txtconcepto_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar >= 33 && e.KeyChar <= 45) || (e.KeyChar <= 47 && e.KeyChar >= 64) || (e.KeyChar >= 91 && e.KeyChar <= 96) || (e.KeyChar >=123 && e.KeyChar <=255))
            {
                MessageBox.Show("Solo Letras", "Alerta", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                e.Handled = true;
                return;
            }
        }

        private void txtpreciounitario_Leave(object sender, EventArgs e)
        {
            int can, pres, total;
            can = Convert.ToInt32(cbcantidad.Text);
            pres = Convert.ToInt32(txtpreciounitario.Text);
            total = can * pres;
            txtpreciototal.Text = total.ToString();
        }
    }
}
