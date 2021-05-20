
namespace NotasSEFI
{
    partial class Frmbienvenido
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Frmbienvenido));
            this.lblSEFI = new System.Windows.Forms.Label();
            this.lblregistracliente = new System.Windows.Forms.Label();
            this.lblquehacer = new System.Windows.Forms.Label();
            this.lblagrega_cliente = new System.Windows.Forms.Label();
            this.lblvernotas = new System.Windows.Forms.Label();
            this.lblcreanota = new System.Windows.Forms.Label();
            this.btncierrasesion = new System.Windows.Forms.Button();
            this.pbcrea = new System.Windows.Forms.PictureBox();
            this.pbver = new System.Windows.Forms.PictureBox();
            this.pbagrega = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pbcrea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbver)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbagrega)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // lblSEFI
            // 
            this.lblSEFI.AutoSize = true;
            this.lblSEFI.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblSEFI.Location = new System.Drawing.Point(216, 67);
            this.lblSEFI.Name = "lblSEFI";
            this.lblSEFI.Size = new System.Drawing.Size(504, 24);
            this.lblSEFI.TabIndex = 26;
            this.lblSEFI.Text = "TALLER MECANICO AUTOMOTRIZ EN GENERAL \"SEFI\"";
            // 
            // lblregistracliente
            // 
            this.lblregistracliente.AutoSize = true;
            this.lblregistracliente.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblregistracliente.Location = new System.Drawing.Point(283, 27);
            this.lblregistracliente.Name = "lblregistracliente";
            this.lblregistracliente.Size = new System.Drawing.Size(330, 24);
            this.lblregistracliente.TabIndex = 25;
            this.lblregistracliente.Text = "Bienvenido al generador de notas del:";
            // 
            // lblquehacer
            // 
            this.lblquehacer.AutoSize = true;
            this.lblquehacer.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblquehacer.Location = new System.Drawing.Point(351, 118);
            this.lblquehacer.Name = "lblquehacer";
            this.lblquehacer.Size = new System.Drawing.Size(177, 24);
            this.lblquehacer.TabIndex = 29;
            this.lblquehacer.Text = "¿Qué desea hacer?";
            // 
            // lblagrega_cliente
            // 
            this.lblagrega_cliente.AutoSize = true;
            this.lblagrega_cliente.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblagrega_cliente.Location = new System.Drawing.Point(30, 414);
            this.lblagrega_cliente.Name = "lblagrega_cliente";
            this.lblagrega_cliente.Size = new System.Drawing.Size(223, 24);
            this.lblagrega_cliente.TabIndex = 32;
            this.lblagrega_cliente.Text = "Agregar un nuevo cliente";
            // 
            // lblvernotas
            // 
            this.lblvernotas.AutoSize = true;
            this.lblvernotas.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblvernotas.Location = new System.Drawing.Point(366, 414);
            this.lblvernotas.Name = "lblvernotas";
            this.lblvernotas.Size = new System.Drawing.Size(168, 24);
            this.lblvernotas.TabIndex = 33;
            this.lblvernotas.Text = "Ver todas las notas";
            // 
            // lblcreanota
            // 
            this.lblcreanota.AutoSize = true;
            this.lblcreanota.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblcreanota.Location = new System.Drawing.Point(669, 414);
            this.lblcreanota.Name = "lblcreanota";
            this.lblcreanota.Size = new System.Drawing.Size(191, 24);
            this.lblcreanota.TabIndex = 34;
            this.lblcreanota.Text = "Crear una nueva nota";
            // 
            // btncierrasesion
            // 
            this.btncierrasesion.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btncierrasesion.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btncierrasesion.Location = new System.Drawing.Point(355, 469);
            this.btncierrasesion.Name = "btncierrasesion";
            this.btncierrasesion.Size = new System.Drawing.Size(192, 45);
            this.btncierrasesion.TabIndex = 35;
            this.btncierrasesion.Text = "Cerrar Sesión";
            this.btncierrasesion.UseVisualStyleBackColor = true;
            this.btncierrasesion.Click += new System.EventHandler(this.btncierrasesion_Click);
            // 
            // pbcrea
            // 
            this.pbcrea.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbcrea.Image = global::NotasSEFI.Properties.Resources.nota;
            this.pbcrea.Location = new System.Drawing.Point(648, 170);
            this.pbcrea.Name = "pbcrea";
            this.pbcrea.Size = new System.Drawing.Size(224, 225);
            this.pbcrea.TabIndex = 31;
            this.pbcrea.TabStop = false;
            this.pbcrea.Click += new System.EventHandler(this.pbcrea_Click);
            // 
            // pbver
            // 
            this.pbver.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbver.Image = global::NotasSEFI.Properties.Resources.ver_notas;
            this.pbver.Location = new System.Drawing.Point(336, 170);
            this.pbver.Name = "pbver";
            this.pbver.Size = new System.Drawing.Size(220, 225);
            this.pbver.TabIndex = 30;
            this.pbver.TabStop = false;
            // 
            // pbagrega
            // 
            this.pbagrega.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbagrega.Image = global::NotasSEFI.Properties.Resources.agrega;
            this.pbagrega.Location = new System.Drawing.Point(27, 170);
            this.pbagrega.Name = "pbagrega";
            this.pbagrega.Size = new System.Drawing.Size(226, 225);
            this.pbagrega.TabIndex = 28;
            this.pbagrega.TabStop = false;
            this.pbagrega.Click += new System.EventHandler(this.pictureBox2_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(27, 17);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(162, 100);
            this.pictureBox1.TabIndex = 27;
            this.pictureBox1.TabStop = false;
            // 
            // Frmbienvenido
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(906, 536);
            this.Controls.Add(this.btncierrasesion);
            this.Controls.Add(this.lblcreanota);
            this.Controls.Add(this.lblvernotas);
            this.Controls.Add(this.lblagrega_cliente);
            this.Controls.Add(this.pbcrea);
            this.Controls.Add(this.pbver);
            this.Controls.Add(this.lblquehacer);
            this.Controls.Add(this.pbagrega);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.lblSEFI);
            this.Controls.Add(this.lblregistracliente);
            this.Name = "Frmbienvenido";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Bienvenido";
            ((System.ComponentModel.ISupportInitialize)(this.pbcrea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbver)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbagrega)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lblSEFI;
        private System.Windows.Forms.Label lblregistracliente;
        private System.Windows.Forms.PictureBox pbagrega;
        private System.Windows.Forms.Label lblquehacer;
        private System.Windows.Forms.PictureBox pbver;
        private System.Windows.Forms.PictureBox pbcrea;
        private System.Windows.Forms.Label lblagrega_cliente;
        private System.Windows.Forms.Label lblvernotas;
        private System.Windows.Forms.Label lblcreanota;
        private System.Windows.Forms.Button btncierrasesion;
    }
}