
namespace NotasSEFI
{
    partial class Frmagreganota
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Frmagreganota));
            this.lblSEFI = new System.Windows.Forms.Label();
            this.lblcantidad = new System.Windows.Forms.Label();
            this.txtconcepto = new System.Windows.Forms.TextBox();
            this.cbcantidad = new System.Windows.Forms.ComboBox();
            this.lblconcepto = new System.Windows.Forms.Label();
            this.lblpreciounitario = new System.Windows.Forms.Label();
            this.lblpreciototal = new System.Windows.Forms.Label();
            this.txtpreciounitario = new System.Windows.Forms.TextBox();
            this.txtpreciototal = new System.Windows.Forms.TextBox();
            this.lblregistracliente = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.btnagrega = new System.Windows.Forms.Button();
            this.btneditar = new System.Windows.Forms.Button();
            this.btnelimina = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // lblSEFI
            // 
            this.lblSEFI.AutoSize = true;
            this.lblSEFI.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblSEFI.Location = new System.Drawing.Point(265, 21);
            this.lblSEFI.Name = "lblSEFI";
            this.lblSEFI.Size = new System.Drawing.Size(504, 24);
            this.lblSEFI.TabIndex = 29;
            this.lblSEFI.Text = "TALLER MECANICO AUTOMOTRIZ EN GENERAL \"SEFI\"";
            // 
            // lblcantidad
            // 
            this.lblcantidad.AutoSize = true;
            this.lblcantidad.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblcantidad.Location = new System.Drawing.Point(72, 183);
            this.lblcantidad.Name = "lblcantidad";
            this.lblcantidad.Size = new System.Drawing.Size(84, 24);
            this.lblcantidad.TabIndex = 32;
            this.lblcantidad.Text = "Cantidad";
            // 
            // txtconcepto
            // 
            this.txtconcepto.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtconcepto.Location = new System.Drawing.Point(199, 219);
            this.txtconcepto.Multiline = true;
            this.txtconcepto.Name = "txtconcepto";
            this.txtconcepto.Size = new System.Drawing.Size(280, 81);
            this.txtconcepto.TabIndex = 31;
            this.txtconcepto.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtconcepto_KeyPress);
            // 
            // cbcantidad
            // 
            this.cbcantidad.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cbcantidad.FormattingEnabled = true;
            this.cbcantidad.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"});
            this.cbcantidad.Location = new System.Drawing.Point(95, 219);
            this.cbcantidad.Name = "cbcantidad";
            this.cbcantidad.Size = new System.Drawing.Size(43, 26);
            this.cbcantidad.TabIndex = 33;
            // 
            // lblconcepto
            // 
            this.lblconcepto.AutoSize = true;
            this.lblconcepto.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblconcepto.Location = new System.Drawing.Point(291, 183);
            this.lblconcepto.Name = "lblconcepto";
            this.lblconcepto.Size = new System.Drawing.Size(92, 24);
            this.lblconcepto.TabIndex = 34;
            this.lblconcepto.Text = "Concepto";
            // 
            // lblpreciounitario
            // 
            this.lblpreciounitario.AutoSize = true;
            this.lblpreciounitario.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblpreciounitario.Location = new System.Drawing.Point(548, 183);
            this.lblpreciounitario.Name = "lblpreciounitario";
            this.lblpreciounitario.Size = new System.Drawing.Size(130, 24);
            this.lblpreciounitario.TabIndex = 35;
            this.lblpreciounitario.Text = "Precio unitario";
            // 
            // lblpreciototal
            // 
            this.lblpreciototal.AutoSize = true;
            this.lblpreciototal.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblpreciototal.Location = new System.Drawing.Point(797, 183);
            this.lblpreciototal.Name = "lblpreciototal";
            this.lblpreciototal.Size = new System.Drawing.Size(102, 24);
            this.lblpreciototal.TabIndex = 36;
            this.lblpreciototal.Text = "Precio total";
            // 
            // txtpreciounitario
            // 
            this.txtpreciounitario.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtpreciounitario.Location = new System.Drawing.Point(552, 231);
            this.txtpreciounitario.Name = "txtpreciounitario";
            this.txtpreciounitario.Size = new System.Drawing.Size(114, 26);
            this.txtpreciounitario.TabIndex = 37;
            this.txtpreciounitario.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtpreciounitario_KeyPress);
            this.txtpreciounitario.Leave += new System.EventHandler(this.txtpreciounitario_Leave);
            // 
            // txtpreciototal
            // 
            this.txtpreciototal.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtpreciototal.Location = new System.Drawing.Point(791, 231);
            this.txtpreciototal.Name = "txtpreciototal";
            this.txtpreciototal.Size = new System.Drawing.Size(114, 26);
            this.txtpreciototal.TabIndex = 38;
            // 
            // lblregistracliente
            // 
            this.lblregistracliente.AutoSize = true;
            this.lblregistracliente.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblregistracliente.Location = new System.Drawing.Point(411, 81);
            this.lblregistracliente.Name = "lblregistracliente";
            this.lblregistracliente.Size = new System.Drawing.Size(178, 24);
            this.lblregistracliente.TabIndex = 28;
            this.lblregistracliente.Text = "Generador de notas";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(75, 21);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(162, 100);
            this.pictureBox1.TabIndex = 30;
            this.pictureBox1.TabStop = false;
            // 
            // btnagrega
            // 
            this.btnagrega.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnagrega.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnagrega.Location = new System.Drawing.Point(129, 428);
            this.btnagrega.Name = "btnagrega";
            this.btnagrega.Size = new System.Drawing.Size(147, 43);
            this.btnagrega.TabIndex = 39;
            this.btnagrega.Text = "Agregar";
            this.btnagrega.UseVisualStyleBackColor = true;
            // 
            // btneditar
            // 
            this.btneditar.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btneditar.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btneditar.Location = new System.Drawing.Point(428, 428);
            this.btneditar.Name = "btneditar";
            this.btneditar.Size = new System.Drawing.Size(147, 43);
            this.btneditar.TabIndex = 40;
            this.btneditar.Text = "Editar";
            this.btneditar.UseVisualStyleBackColor = true;
            // 
            // btnelimina
            // 
            this.btnelimina.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnelimina.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnelimina.Location = new System.Drawing.Point(738, 428);
            this.btnelimina.Name = "btnelimina";
            this.btnelimina.Size = new System.Drawing.Size(147, 43);
            this.btnelimina.TabIndex = 41;
            this.btnelimina.Text = "Eliminar";
            this.btnelimina.UseVisualStyleBackColor = true;
            // 
            // Frmagreganota
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(964, 534);
            this.Controls.Add(this.btnelimina);
            this.Controls.Add(this.btneditar);
            this.Controls.Add(this.btnagrega);
            this.Controls.Add(this.txtpreciototal);
            this.Controls.Add(this.txtpreciounitario);
            this.Controls.Add(this.lblpreciototal);
            this.Controls.Add(this.lblpreciounitario);
            this.Controls.Add(this.lblconcepto);
            this.Controls.Add(this.cbcantidad);
            this.Controls.Add(this.lblcantidad);
            this.Controls.Add(this.txtconcepto);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.lblSEFI);
            this.Controls.Add(this.lblregistracliente);
            this.Name = "Frmagreganota";
            this.Text = "Crear nueva nota";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lblSEFI;
        private System.Windows.Forms.Label lblcantidad;
        private System.Windows.Forms.TextBox txtconcepto;
        private System.Windows.Forms.ComboBox cbcantidad;
        private System.Windows.Forms.Label lblconcepto;
        private System.Windows.Forms.Label lblpreciounitario;
        private System.Windows.Forms.Label lblpreciototal;
        private System.Windows.Forms.TextBox txtpreciounitario;
        private System.Windows.Forms.TextBox txtpreciototal;
        private System.Windows.Forms.Label lblregistracliente;
        private System.Windows.Forms.Button btnagrega;
        private System.Windows.Forms.Button btneditar;
        private System.Windows.Forms.Button btnelimina;
    }
}