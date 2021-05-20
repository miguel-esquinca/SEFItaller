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
    public partial class Frmbienvenido : Form
    {
        public Frmbienvenido()
        {
            InitializeComponent();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            Form formulario = new frmCliente();
            formulario.Show();
        }

        private void btncierrasesion_Click(object sender, EventArgs e)
        {
          
        }

        private void pbcrea_Click(object sender, EventArgs e)
        {
            Form crea = new Frmagreganota();
            crea.Show();
        }
    }
}
