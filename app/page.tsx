import { Sidebar } from "@/components/sidebar";
import { StatsCard } from "@/components/stats-card";
import { PatientsTable } from "@/components/patients-table";
import { Users, PawPrint, Calendar } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-background">
      <Sidebar />

      {/* Main Content */}
      <main className="lg:pl-64">
        {/* Header */}
        <header className="border-b border-border bg-card px-6 py-6 lg:px-8">
          <div className="ml-12 lg:ml-0">
            <h1 className="text-2xl font-bold tracking-tight text-foreground">
              Dashboard
            </h1>
            <p className="mt-1 text-sm text-muted-foreground">
              Bienvenido de vuelta, Dr. Rodriguez. Aqui esta el resumen de hoy.
            </p>
          </div>
        </header>

        {/* Content */}
        <div className="p-6 lg:p-8">
          {/* Stats Cards */}
          <section className="mb-8">
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              <StatsCard
                title="Total Clientes"
                value={248}
                icon={Users}
                trend={{ value: 12, isPositive: true }}
                variant="primary"
              />
              <StatsCard
                title="Pacientes Activos"
                value={156}
                icon={PawPrint}
                trend={{ value: 8, isPositive: true }}
                variant="accent"
              />
              <StatsCard
                title="Visitas Hoy"
                value={12}
                icon={Calendar}
                trend={{ value: 3, isPositive: false }}
                variant="default"
              />
            </div>
          </section>

          {/* Patients Table */}
          <section>
            <PatientsTable />
          </section>
        </div>
      </main>
    </div>
  );
}
